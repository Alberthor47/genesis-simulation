import genesis as gs
import numpy as np

def init_ball_and_plate_scene():
    gs.init(backend=gs.cpu)

    scene = gs.Scene(
      show_viewer = True
    )

    floor = scene.add_entity(
        gs.morphs.Plane(),
    )

    # ball = scene.add_entity(
    #     gs.morphs.Sphere(radius=0.1, color=(1, 0, 0)),
    # )

    cam = scene.add_camera(
        res    = (640, 480),
        pos    = (3.5, 0.0, 2.5),
        lookat = (0, 0, 0.5),
        fov    = 30,
        GUI    = False,
    )

    scene.build()
    return scene

def simulate(scene):
    for i in range(1000):
        scene.step()

def main():
    scene = init_ball_and_plate_scene()

    gs.tools.run_in_another_thread(fn=simulate, args=(scene,))
    scene.viewer.start()

if __name__ == "__main__":
    main()
