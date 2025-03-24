import genesis as gs
import numpy as np

SIMULATION_TIME = 400

def main():
    gs.init(backend=gs.cpu)

    scene = gs.Scene(
        show_viewer = False,
    )

    floor = scene.add_entity(
        gs.morphs.Plane(),
    )

    plate = scene.add_entity(
        gs.morphs.URDF(
            file='robot/plate.urdf',
            pos=(0, 0, 0.5),
        ),
    )

    cam = scene.add_camera(
        res    = (640, 480),
        pos    = (3.5, 0.0, 2.5),
        lookat = (0, 0, 0.5),
        fov    = 30,
        GUI    = False,
    )

    scene.build()
    gs.tools.run_in_another_thread(fn=run_sim, args=(scene, cam))
    cam.start_recording()

def run_sim(scene, cam):
    for i in range(SIMULATION_TIME):
        scene.step()
        cam.render()
    cam.stop_recording(save_to_filename='out/plate.mp4', fps=60)

if __name__ == "__main__":
    main()