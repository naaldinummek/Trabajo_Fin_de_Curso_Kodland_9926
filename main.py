# main.py
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import climate_classifications

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Dictionary mapping climate classes to modules
CLIMATES = {
    'A': (
        'Tropical', climate_classifications.get_tropical,
        climate_classifications.list_tropical_subclasses,
        climate_classifications.get_tropical_plants
        ),
    'B': (
        'Arid', climate_classifications.get_arid,
        climate_classifications.list_arid_subclasses,
        climate_classifications.get_arid_plants
        ),
    'C': (
        'Temperate', climate_classifications.get_temperate,
        climate_classifications.list_temperate_subclasses,
        climate_classifications.get_temperate_plants
        ),
    'D': (
        'Continental', climate_classifications.get_continental,
        climate_classifications.list_continental_subclasses,
        climate_classifications.get_continental_plants
        ),
    'E': (
        'Polar', climate_classifications.get_polar,
        climate_classifications.list_polar_subclasses,
        climate_classifications.get_polar_plants
        ),
}

# =====================
# BOT EVENTS
# =====================


@bot.event
async def on_ready():
    """Bot startup event"""
    print(f'✅ Bot connected as {bot.user}')
    print(f'📊 Total servers: {len(bot.guilds)}')
    try:
        synced = await bot.tree.sync()
        print(f'🔄 Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Error syncing commands: {e}')

# =====================
# SLASH COMMANDS
# =====================


@bot.tree.command(name="start",
                  description="Welcome to the Climate & Plant Bot!")
async def start(interaction: discord.Interaction):
    """Main startup command with climate selection"""
    embed = discord.Embed(
        title="🌍 Köppen-Geiger Climate Classification Bot",
        description=(
            "Select a climate class to explore native plants for reforestation"
        ),
        color=discord.Color.green()
    )

    embed.add_field(
        name="Available Climate Classes:",
        value=(
            "**[A]** Tropical - Year-round warmth and rainfall\n"
            "**[B]** Arid - Dry deserts and steppes\n"
            "**[C]** Temperate - Moderate climates\n"
            "**[D]** Continental - Extreme seasons, very cold winters\n"
            "**[E]** Polar - Frozen regions, tundra and ice"
        ),
        inline=False
    )

    embed.add_field(
        name="💡 How to use:",
        value=(
            "Use `/subclasses <A|B|C|D|E>` to see subcategories\n"
            "Use `/plants <code>` (e.g., `/plants Af`) to see species"
        ),
        inline=False
    )

    embed.set_footer(text="Fight climate change through reforestation")
    await interaction.response.send_message(embed=embed)

# =====================


@bot.tree.command(name="subclasses", description="View climate subclasses")
async def subclasses(interaction: discord.Interaction, climate_class: str):
    """Show subcategories for a climate class"""
    climate_class = climate_class.upper()

    if climate_class not in CLIMATES:
        await interaction.response.send_message(
            "❌ Invalid climate class. Use: A, B, C, D, or E",
            ephemeral=True
        )
        return

    class_name, get_single, list_func, _ = CLIMATES[climate_class]

    embed = discord.Embed(
        title=f"Climate Class {climate_class}: {class_name}",
        color=discord.Color.blue()
    )

    codes = list_func()
    for code in codes:
        subclass_data = get_single(code)
        embed.add_field(
            name=f"**{code}** - {subclass_data['name']}",
            value=(
                f"{subclass_data['description']}\n"
                f"🌧️ Rainfall: {subclass_data['annual_rainfall']}\n"
                f"🌡️ Temp: {subclass_data['avg_temperature']}"
            ),
            inline=False
        )

    await interaction.response.send_message(embed=embed)

# =====================


@bot.tree.command(
    name="plants", description="View plants for a climate subclass"
)
async def plants(interaction: discord.Interaction, code: str):
    """Show plants for a specific climate code (e.g., 'Af', 'BWh', 'Csa')"""
    code = code.strip()

    # Determine which climate class
    climate_letter = code[0].upper()

    if climate_letter not in CLIMATES:
        await interaction.response.send_message(
            "❌ Invalid climate code. Start with A, B, C, D, or E",
            ephemeral=True
        )
        return

    (
        class_name,
        get_climate_func,
        list_func,
        get_plants_func,
    ) = CLIMATES[climate_letter]

    climate_info = get_climate_func(code)
    if not climate_info:
        await interaction.response.send_message(
            f"❌ Climate code '{code}' not found. Use `/subclasses "
            f"{climate_letter}` to see valid codes",
            ephemeral=True
        )
        return

    plants_list = get_plants_func(code)

    embed = discord.Embed(
        title=f"{code} - {climate_info['name']}",
        description=climate_info['description'],
        color=discord.Color.green()
    )

    embed.add_field(
        name="📊 Climate Data",
        value=(
            f"**Rainfall:** {climate_info['annual_rainfall']}\n"
            f"**Temperature:** {climate_info['avg_temperature']}"
        ),
        inline=False,
    )

    embed.add_field(
        name=f"🌱 Native Plants ({len(plants_list)})",
        value="⠀",
        inline=False,
    )

    for plant in plants_list:
        plant_text = (
            f"**{plant['name']}**\n"
            f"_{plant['description']}_\n"
            f"🚨 Conservation Status: {plant['extinction_risk']}"
        )
        embed.add_field(name="⠀", value=plant_text, inline=False)

    await interaction.response.send_message(embed=embed)

# =====================


@bot.tree.command(
    name="plant_info", description="Detailed info about a specific plant"
)
async def plant_info(interaction: discord.Interaction, plant_name: str):
    """Search for a plant across all climates"""
    plant_name = plant_name.lower()
    found = False

    for climate_letter, (
        class_name, get_single, list_func, get_plants_func
    ) in CLIMATES.items():
        codes = list_func()
        for code in codes:
            plants_list = get_plants_func(code)

            for plant in plants_list:
                if plant_name in plant['name'].lower():
                    embed = discord.Embed(
                        title=plant['name'],
                        description=plant['description'],
                        color=discord.Color.gold()
                    )

                    embed.add_field(
                        name="🌍 Climate Zone",
                        value=f"{code} ({class_name})",
                        inline=False,
                    )
                    embed.add_field(
                        name="🚨 Extinction Risk",
                        value=plant['extinction_risk'],
                        inline=True,
                    )

                    await interaction.response.send_message(embed=embed)
                    found = True
                    return

    if not found:
        await interaction.response.send_message(
            f"❌ Plant '{plant_name}' not found in database",
            ephemeral=True
        )

# =====================


@bot.tree.command(
    name="random_plant", description="Get a random plant recommendation"
)
async def random_plant(interaction: discord.Interaction):
    """Random plant from any climate"""
    import random

    all_plants = []
    all_codes = []

    for (
        climate_letter,
        (class_name, get_single, list_func, get_plants_func),
    ) in CLIMATES.items():
        codes = list_func()
        for code in codes:
            plants_list = get_plants_func(code)
            all_plants.extend(plants_list)
            all_codes.extend([code] * len(plants_list))

    if not all_plants:
        await interaction.response.send_message(
            "❌ No plants in database",
            ephemeral=True
        )
        return

    idx = random.randint(0, len(all_plants) - 1)
    plant = all_plants[idx]
    code = all_codes[idx]

    embed = discord.Embed(
        title="🎲 Random Plant Recommendation",
        color=discord.Color.random()
    )

    embed.add_field(name="🌱 Plant", value=plant['name'], inline=False)
    embed.add_field(name="📝 Description", value=plant['description'],
                    inline=False)
    embed.add_field(name="🌍 Climate Zone", value=code, inline=True)
    embed.add_field(name="🚨 Status", value=plant['extinction_risk'],
                    inline=True)

    await interaction.response.send_message(embed=embed)

# =====================


@bot.tree.command(name="list_all",
                  description="List all available climate codes")
async def list_all(interaction: discord.Interaction):
    """Show all available climate codes"""
    embed = discord.Embed(
        title="📋 All Köppen-Geiger Climate Codes",
        color=discord.Color.blue()
    )

    for climate_letter, (
        class_name, get_single, list_func, _
    ) in CLIMATES.items():
        codes = ", ".join(list_func())
        embed.add_field(
            name=f"{climate_letter} - {class_name}",
            value=f"`{codes}`",
            inline=False
        )

    embed.set_footer(text="Use /plants <code> to view species")
    await interaction.response.send_message(embed=embed)

# =====================


@bot.tree.command(name="help", description="Show all available commands")
async def help_command(interaction: discord.Interaction):
    """Help menu"""
    embed = discord.Embed(
        title="📚 Bot Commands",
        color=discord.Color.purple()
    )

    commands_list = [
        ("**/start**", "Welcome message and climate overview"),
        ("**/subclasses <A|B|C|D|E>**",
            "Show subcategories for a climate class"),
        ("**/plants <code>**",
            "View plants for a climate (e.g., Af, BWh, Csa)"),
        ("**/plant_info <name>**", "Search for a specific plant"),
        ("**/random_plant**", "Get a random plant recommendation"),
        ("**/list_all**", "Show all available climate codes"),
        ("**/help**", "This help menu"),
    ]

    for command, description in commands_list:
        embed.add_field(name=command, value=description, inline=False)

    embed.set_footer(text="🌍 Fighting climate change through reforestation")
    await interaction.response.send_message(embed=embed)

# =====================
# RUN BOT
# =====================

if __name__ == "__main__":
    bot.run(
        'TOKEN'
    )  # Replace with your actual token
