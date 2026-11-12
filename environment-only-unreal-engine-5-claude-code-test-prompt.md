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

### Level layout and progression

Build a deliberate transition from a confined, directed opening to a broad, exposed outdoor space.

1. **Starting room:** Place the host player's start in a room with only one usable exit. The player must leave in one direction and enter the intended route.
2. **One route through Warehouses 1 and 2:** Force the player along one continuous forward route through the first warehouse and then the second. Block side routes with believable industrial arrangements made from the available assets: concrete barriers, shipping containers, stacked crates, parked equipment, fences, and other suitable objects. These obstructions must look naturally placed in the facility and physically prevent bypassing the route. Avoid arbitrary invisible walls or artificial-looking corridor walls. Preserve the existing warehouse identities, including Warehouse 2's catwalk; any accessible side space must not provide a route around the required sequence.
3. **Warehouse 2 encounter — future gameplay intent:** The second warehouse will contain five riflemen. Defeating all five will open access to the outdoor area. Plan the exit and its surrounding layout to support that future progression gate. For this environment-only walkthrough, keep the exit passable so the whole layout can be explored without enemies or combat.
4. **Open-yard reveal:** After Warehouse 2, the environment should suddenly open up and feel as though the player can run in any direction. Remove the close flanking barricades used in the opening route and provide a broad, traversable outdoor yard with room to move freely.
5. **Distant sniper warehouse:** Use Warehouse 3, the freight storage warehouse already designated for future rooftop sniper positions, as the distant warehouse across this yard. Place it far enough away to create a clearly substantial, exposed crossing. Place additional background structures and industrial scenery much farther beyond it to establish depth and scale. Background scenery does not all need to be reachable. Keep Warehouse 4 in the overall compound without compromising the open-yard reveal; its exact position is not yet specified.
6. **Small safe area outside the exit:** Allow the player to step slightly outside Warehouse 2 into a small bubble of safety before entering the exposed yard. Compose the exit, nearby cover, and rooftop sightlines so this staging area and the distant threat position can be evaluated during the walkthrough.
7. **Sniper response — future gameplay intent:** Once the player leaves that small safe area, all snipers on the distant warehouse roof should aggro. Record this intended boundary and behavior in the implementation handoff. Do not implement snipers, AI, damage, combat, or an active aggro trigger in this environment-only test.

Exact crossing distances, safe-area size, and sniper count have not been specified. Treat initial dimensions as adjustable layout choices, not fixed requirements. The safe-area boundary is a future gameplay boundary, not a physical wall that prevents exploration.

**Walkthrough verification:** Confirm that the start has only one usable exit, side obstructions cannot be bypassed to skip the first two warehouses, and the route opens into a genuinely broad yard after Warehouse 2. Walk slightly outside the exit to assess the small safe staging area, then cross the yard to evaluate the distant warehouse, rooftop sightlines, and much farther background scenery. The full walkthrough must remain possible without defeating enemies.

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