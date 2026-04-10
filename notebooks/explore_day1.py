import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('cache/')

print("Loading session...")
session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()
print("Session loaded!")

lando = session.laps.pick_drivers('NOR')  # updated to new version
print(lando.head())

# --- CHART ---
# Drop laps where LapTime is missing (e.g. lap 1, safety car laps)
lando_clean = lando.dropna(subset=['LapTime'])

lap_numbers = lando_clean['LapNumber']
lap_times = lando_clean['LapTime'].dt.total_seconds()

plt.figure(figsize=(12, 50))
plt.plot(lap_numbers, lap_times, color= "#E86D26", linewidth=2, marker='o', markersize=3)
plt.title("Lando Norris — Lap Times, Monaco 2024")
plt.xlabel("Lap")
plt.ylabel("Lap Time (seconds)")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig('lando_monaco.png')
print("Chart saved as lando_monaco.png!")
plt.show()