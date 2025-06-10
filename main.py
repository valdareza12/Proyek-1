from manim import *

class LoveShape(Scene):
    def construct(self):
        # Parametric heart shape
        heart = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t)**3,
                13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                0
            ]) * 0.1,  # Scale down
            t_range = [0, TAU],
            color = RED,
            stroke_width = 6
        )

        # Fill with a pink shade
        heart_fill = heart.copy().set_fill(RED, opacity=0.5).set_stroke(width=0)

        # Group fill and stroke
        heart_group = VGroup(heart_fill, heart)

        # Center and scale
        heart_group.move_to(ORIGIN)

        # Animate the heart
        self.play(DrawBorderThenFill(heart_group))
        self.wait(2)
        