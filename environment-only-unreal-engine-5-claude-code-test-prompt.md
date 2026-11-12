You are the lead Unreal Engine 5 environment developer for **603 Interactive**.

I want to test whether you can build our game's physical environment using the assets we've collected.

**GitHub Repository:** https://github.com/603interactive/Insurgency-

**Asset Reference:** `ASSET_LINKS.md`

### Your objective

Create a **fully explorable 3D industrial warehouse compound** in Unreal Engine 5 using the free Fab assets listed in our GitHub repository.

Build the environment we designed:

1. **Warehouse 1:** Small receiving warehouse with loading docks, storage crates, and industrial clutter.
2. **Warehouse 2:** Large assembly warehouse with a second-floor catwalk overlooking the ground floor.
3. **Warehouse 3:** Freight storage warehouse with an accessible rooftop suitable for future sniper positions.
4. **Warehouse 4:** Industrial control building with a control room and space for a future final objective.

Connect all four buildings using realistic outdoor industrial yards containing shipping containers, forklifts, construction equipment, fences, concrete barriers, gravel, and asphalt.

**Visual direction:** Gritty, realistic, abandoned industrial facility. Overcast sky, subtle fog, believable lighting, detailed environmental materials, and strong visual atmosphere.

### Critical requirements

- Use the actual Fab assets referenced in `ASSET_LINKS.md`, not just placeholder geometry.
- Check which assets are installed and accessible. Do not claim assets have been imported unless verified.
- Build one connected, explorable level.
- Add a basic first-person walking camera with WASD movement, mouse look, and collision so I can explore the environment.
- **DO NOT implement enemies, AI, combat, weapons, inventory, shops, missions, or other gameplay mechanics.**
- Prioritize environmental quality, proper scale, lighting, and performance.
- If assets are unavailable, explain what's missing rather than pretending to use them.
- Work within the existing Unreal project, if present. Do not overwrite unrelated files.

### Deliverable

I want to open Unreal Engine, press **Play**, and freely walk through all four warehouses and their surrounding outdoor areas.

Use the existing 603 Interactive specialist agents where available. Verify the actual environment before claiming completion.

**Important:** This is an environment-only prototype. Do not modify `DEVLOG.md`, and do not begin implementing the full game. Build only what's necessary to let me walk around and evaluate the world.