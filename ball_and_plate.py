import genesis as gs

SIMULATION_TIME = 600

def init_scene_and_cam():
    gs.init(backend=gs.cpu)

    scene = gs.Scene(show_viewer=False)

    # Floor as the ground.
    floor = scene.add_entity(gs.morphs.Plane())

    # Ball as a URDF file.
    ball = scene.add_entity(
        # gs.morphs.URDF(
        #     file='robot/ball.urdf',
        #     pos=(0, 0, 0.5),
        # ),
        gs.morphs.Sphere(
            pos=(0, 0, 1),
            radius=0.1,
        ),
    )

    # Plate as a URDF file.
    plate = scene.add_entity(
        gs.morphs.URDF(
            file='robot/plate.urdf',
            pos=(0, 0, 0.25),
        ),
    )

    # # Create a static base for the plate support.
    # base = scene.add_entity(
    #     gs.morphs.Box(pos=(0, 0, 1), size=(0.1, 0.1, 0.1))
    # )

    # Add a camera.
    cam = scene.add_camera(
        res    = (1280, 960),
        pos    = (4, 0.0, 2),
        lookat = (0, 0, 0),
        fov    = 50,
    )

    return scene, cam

def simulate(scene, cam):
    for i in range(SIMULATION_TIME):
        scene.step()
        cam.render()
    cam.stop_recording(save_to_filename='out/b&p.mp4', fps=60)

def main():
    scene, cam = init_scene_and_cam()
    scene.build()
    gs.tools.run_in_another_thread(fn=simulate, args=(scene, cam))
    cam.start_recording()

if __name__ == "__main__":
    main()
