import pyglet
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyApplication(arcade.Window):
    def setup(self):
        self.bm = arcade.sound.load_sound("PuertoRico.wav")
        self.click_sound = arcade.load_sound("hello.mp3")
        self.stop_bm = False
        self.player = pyglet.media.Player()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Looped Background Music", SCREEN_WIDTH/2-160, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, 20)
        arcade.draw_text("Try clicking", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-35,
                         arcade.color.WHITE, 14)
        self.update_sound()

    def update_sound(self):
        if not self.player.playing:
            self.player.queue(self.bm)
            self.player.play()

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.click_sound)

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()
arcade.run()