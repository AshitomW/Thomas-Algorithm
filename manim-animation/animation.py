from manim import *




class StartingScreen(Scene):
    def construct(self):
        title = Text("Thomas Tridiagonal Algorithm",font_size=48)
        subtitle = Text("An Introduction to Thomas Algorithm", font_size=24).next_to(title,DOWN)

        title.move_to(UP * 0.5 )

        self.play(Write(title),run_time=2)
        self.play(FadeIn(subtitle),run_time=2)



        self.wait(2)


        self.play(FadeOut(title),FadeOut(subtitle),run_time=2)







class SystemOfEquationsMatrix(Scene):
    def construct(self):
        # Create the "Example" label
        example_label = Text("Example").to_edge(UP)
        
        # Create the system of equations as text
        eq1 = Text("4x - y = 2")
        eq2 = Text("-x + 4y - z = 4")
        eq3 = Text("-y + 4z = 10")

        # Position the equations below the "Example" label
        eq1.next_to(example_label, DOWN, buff=0.5)
        eq2.next_to(eq1, DOWN)
        eq3.next_to(eq2, DOWN)

        # Display the "Example" label and system of equations
        self.play(Write(example_label))
        self.play(Write(eq1), Write(eq2), Write(eq3))
        self.wait(2)

        # Create the coefficient matrix
        coefficient_matrix = Matrix(
            [[4, -1, 0],
             [-1, 4, -1],
             [0, -1, 4]],
            left_bracket="[", right_bracket="]"
        )

        # Create the variable matrix
        variable_matrix = Matrix(
            [["x"], ["y"], ["z"]],
            left_bracket="[", right_bracket="]"
        )

        # Create the constants matrix
        constants_matrix = Matrix(
            [[2], [4], [10]],
            left_bracket="[", right_bracket="]"
        )

        # Create the equation with matrices using a dot instead of ×
        matrix_group = VGroup(
            coefficient_matrix, Text("⋅").scale(1.5), variable_matrix, Text("=").scale(1.5), constants_matrix
        ).arrange(RIGHT, buff=0.5)

        # Position the matrix group below the system of equations
        matrix_group.next_to(eq3, DOWN, buff=1)

        # Display the matrix form of the equations
        self.play(Write(coefficient_matrix), Write(variable_matrix), Write(constants_matrix))
        self.play(Write(matrix_group[1]), Write(matrix_group[3]))
        self.wait(2)



        # Add a title for clarity
        title = Text("Thomas Tridiagonal Matrix Form").to_edge(UP)
        self.play(Transform(example_label, title))
        self.wait(2)

        self.clear()

        self.play(FadeOut(example_label), FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(matrix_group))

        # Create the tridiagonal matrix again
        coefficient_matrix_new = Matrix(
            [[4, -1, 0],
             [-1, 4, -1],
             [0, -1, 4]],
            left_bracket="[", right_bracket="]"
        )

        # Create the variable matrix
        variable_matrix_new = Matrix(
            [["x"], ["y"], ["z"]],
            left_bracket="[", right_bracket="]"
        )

        # Create the constants matrix
        constants_matrix_new = Matrix(
            [[2], [4], [10]],
            left_bracket="[", right_bracket="]"
        )

        # Create the equation with matrices using a dot instead of ×
        matrix_group_new = VGroup(
            coefficient_matrix_new, Text("⋅").scale(1.5), variable_matrix_new, Text("=").scale(1.5), constants_matrix_new
        ).arrange(RIGHT, buff=0.5)

        # Position the matrix group below the previous content
        matrix_group_new.shift(UP)

        # Display the tridiagonal matrix
        self.play(Write(coefficient_matrix_new), Write(variable_matrix_new), Write(constants_matrix_new))
        self.play(Write(matrix_group_new[1]), Write(matrix_group_new[3]))
        self.wait(2)

        # Highlight the main diagonal
        main_diagonal_elements = VGroup(
            coefficient_matrix_new.get_entries()[0],  # 4
            coefficient_matrix_new.get_entries()[4],  # 4
            coefficient_matrix_new.get_entries()[8]   # 4
        )
        main_diagonal_highlight = VGroup()
        for element in main_diagonal_elements:
            highlight = SurroundingRectangle(element, color=YELLOW, buff=0.1)
            main_diagonal_highlight.add(highlight)

        # Highlight the upper diagonal
        upper_diagonal_elements = VGroup(
            coefficient_matrix_new.get_entries()[1],  # -1
            coefficient_matrix_new.get_entries()[5]   # -1
        )
        upper_diagonal_highlight = VGroup()
        for element in upper_diagonal_elements:
            highlight = SurroundingRectangle(element, color=BLUE, buff=0.1)
            upper_diagonal_highlight.add(highlight)

        # Highlight the lower diagonal
        lower_diagonal_elements = VGroup(
            coefficient_matrix_new.get_entries()[3],  # -1
            coefficient_matrix_new.get_entries()[7]   # -1
        )
        lower_diagonal_highlight = VGroup()
        for element in lower_diagonal_elements:
            highlight = SurroundingRectangle(element, color=RED, buff=0.1)
            lower_diagonal_highlight.add(highlight)

        # Animate highlighting the diagonals
        self.play(Create(main_diagonal_highlight))
        self.play(Create(upper_diagonal_highlight))
        self.play(Create(lower_diagonal_highlight))
        self.wait(2)
        yellow_dot = Dot(color=YELLOW).shift(DOWN + LEFT * 3)
        blue_dot = Dot(color=BLUE).next_to(yellow_dot, DOWN, buff=0.5)
        red_dot = Dot(color=RED).next_to(blue_dot, DOWN, buff=0.5)

        # Add the labels
        upper_diagonal_label = MathTex("Upper Diagonal (c)(first element:c_{1})",font_size=24).next_to(blue_dot, RIGHT, buff=0.5)
        main_diagonal_label = MathTex("Main Diagonal (b)(first element: b_{1})",font_size=24).next_to(yellow_dot, RIGHT, buff=0.5)
        lower_diagonal_label = MathTex("Lower Diagonal (a)(first element: a_{2})",font_size=24).next_to(red_dot, RIGHT, buff=0.5)

        # Display the color dots and their labels
        self.play(FadeIn(blue_dot),FadeIn(yellow_dot),FadeIn(red_dot))
        self.play(Write(upper_diagonal_label),Write(main_diagonal_label), Write(lower_diagonal_label))

        self.wait(5)






class ThomasTridiagonalStep1(Scene):
    def construct(self):
        # Title for the scene with smaller font size
        title = Text("Thomas Tridiagonal System - Step 1", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Step 1: Draw the coefficient matrix with reduced font size
        coefficient_matrix = Matrix(
            [[4, -1, 0],
             [-1, 4, -1],
             [0, -1, 4]],
            left_bracket="[", right_bracket="]"
        ).shift(UP*1.2)

        # Display the coefficient matrix
        self.play(Write(coefficient_matrix))
        self.wait(2)

        # Step 1: Text for the α values with increased spacing and smaller font size
        step_text = Text("Step 1: Set α1 = b1 = 4 and compute α2, α3", font_size=30).shift(DOWN * 1.2)
        self.play(Write(step_text))
        self.wait(1)

        # Compute α2 = b2 - (a2 * c1) / α1 = 4 - (-1 * -1) / 4 = 4 - 1/4 = 15/4
        alpha_2_formula = MathTex(
            r"\alpha_2 = b_2 - \frac{a_2 c_1}{\alpha_1} = 4 - \frac{(-1) \cdot (-1)}{4} = \frac{15}{4}",
            font_size=28
        ).shift(DOWN * 2)
        self.play(Write(alpha_2_formula))
        self.wait(2)

        # Compute α3 = b3 - (a3 * c2) / α2 = 4 - (-1 * -1) / (15/4) = 4 - 1/(15/4) = 56/15
        alpha_3_formula = MathTex(
            r"\alpha_3 = b_3 - \frac{a_3 c_2}{\alpha_2} = 4 - \frac{(-1) \cdot (-1)}{\frac{15}{4}} = \frac{56}{15}",
            font_size=28
        ).shift(DOWN * 3)
        self.play(Write(alpha_3_formula))
        self.wait(2)

        # Fade out all after the calculations
        self.play(FadeOut(coefficient_matrix), FadeOut(step_text), FadeOut(alpha_2_formula), FadeOut(alpha_3_formula))





class ThomasTridiagonalStep2(Scene):
    def construct(self):
        # Title for the scene with smaller font size
        title = Text("Thomas Tridiagonal System - Step 2", font_size=28).to_edge(UP)
        self.play(Write(title))
        self.wait(1)


        coefficient_matrix = Matrix(
            [[4, -1, 0],
             [-1, 4, -1],
             [0, -1, 4]],
            left_bracket="[", right_bracket="]"
        ).shift(UP*1.3).scale(0.7)

        # Display the coefficient matrix
        self.play(Write(coefficient_matrix))
        self.wait(2)



        # Step 2: Text for the β values with increased spacing and smaller font size
        step_text = Text("Step 2: Set β1 = d1 / b1 = 2 / 4 = 1/2 and compute β2, β3", font_size=23).shift(DOWN * 0.5)
        self.play(Write(step_text))
        self.wait(1)

        # Compute β1 = d1 / b1 = 2 / 4 = 1/2
        beta_1_formula = MathTex(
            r"\beta_1 = \frac{d_1}{b_1} = \frac{2}{4} = \frac{1}{2}",
            font_size=23
        ).shift(DOWN * 1.05)
        self.play(Write(beta_1_formula))
        self.wait(2)

        # Compute β2 = d2 - (a2 * β1) / α2 = 4 - (-1 * 1/2) / (15/4) = 6/5
        beta_2_formula = MathTex(
            r"\beta_2 = \frac{d_2 - a_2 \beta_1}{\alpha_2} = \frac{4 - (-1) \cdot \frac{1}{2}}{\frac{15}{4}} = \frac{6}{5}",
            font_size=23
        ).shift(DOWN * 1.8 )
        self.play(Write(beta_2_formula))
        self.wait(2)

        # Compute β3 = d3 - (a3 * β2) / α3 = 10 - (-1 * 6/5) / (56/15) = 3
        beta_3_formula = MathTex(
            r"\beta_3 = \frac{d_3 - a_3 \beta_2}{\alpha_3} = \frac{10 - (-1) \cdot \frac{6}{5}}{\frac{56}{15}} = 3",
            font_size=23
        ).shift(DOWN * 2.6)
        self.play(Write(beta_3_formula))
        self.wait(2)

        # Fade out all after the calculations
        self.play(FadeOut(step_text), FadeOut(beta_1_formula), FadeOut(beta_2_formula), FadeOut(beta_3_formula))




class ThomasTridiagonalStep2(Scene):
    def construct(self):
        # Title for the scene with smaller font size
        title = Text("Thomas Tridiagonal System - Step 2", font_size=28).to_edge(UP)
        self.play(Write(title))
        self.wait(1)


        coefficient_matrix = Matrix(
            [[4, -1, 0],
             [-1, 4, -1],
             [0, -1, 4]],
            left_bracket="[", right_bracket="]"
        ).shift(UP*1.3).scale(0.7)

        # Display the coefficient matrix
        self.play(Write(coefficient_matrix))
        self.wait(2)



        # Step 2: Text for the β values with increased spacing and smaller font size
        step_text = Text("Step 2: Set β1 = d1 / b1 = 2 / 4 = 1/2 and compute β2, β3", font_size=23).next_to(coefficient_matrix, DOWN, buff=0.2)
        self.play(Write(step_text))
        self.wait(1)

        # Compute β1 = d1 / b1 = 2 / 4 = 1/2
        beta_1_formula = MathTex(
            r"\beta_1 = \frac{d_1}{b_1} = \frac{2}{4} = \frac{1}{2}",
            font_size=23
        ).shift(DOWN * 1.05)
        self.play(Write(beta_1_formula))
        self.wait(2)

        # Compute β2 = d2 - (a2 * β1) / α2 = 4 - (-1 * 1/2) / (15/4) = 6/5
        beta_2_formula = MathTex(
            r"\beta_2 = \frac{d_2 - a_2 \beta_1}{\alpha_2} = \frac{4 - (-1) \cdot \frac{1}{2}}{\frac{15}{4}} = \frac{6}{5}",
            font_size=23
        ).shift(DOWN * 1.8 )
        self.play(Write(beta_2_formula))
        self.wait(2)

        # Compute β3 = d3 - (a3 * β2) / α3 = 10 - (-1 * 6/5) / (56/15) = 3
        beta_3_formula = MathTex(
            r"\beta_3 = \frac{d_3 - a_3 \beta_2}{\alpha_3} = \frac{10 - (-1) \cdot \frac{6}{5}}{\frac{56}{15}} = 3",
            font_size=23
        ).shift(DOWN * 2.6)
        self.play(Write(beta_3_formula))
        self.wait(2)

        # Fade out all after the calculations
        self.play(FadeOut(step_text), FadeOut(beta_1_formula), FadeOut(beta_2_formula), FadeOut(beta_3_formula))


class ThomasTridiagonalFinalStepDirect(Scene):
    def construct(self):
        # Title for the final step with smaller font size
        title = Text("Thomas Tridiagonal System - Final Step", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create and display the coefficient matrix again for reference
        coefficient_matrix = Matrix(
            [[4, -1, 0],
             [-1, 4, -1],
             [0, -1, 4]],
            left_bracket="[", right_bracket="]"
        ).shift(UP * 1.5)

        # Display the coefficient matrix
        self.play(Write(coefficient_matrix))
        self.wait(2)

        # Step Text for u3 = z, with reduced gap and smaller font size
        step_text_u3 = Text("Step 1: Compute u3 = z", font_size=24).next_to(coefficient_matrix, DOWN, buff=0.2)
        self.play(Write(step_text_u3))
        self.wait(1)

        # Directly compute and display the result for u3 = z
        u_3_result = MathTex(
            r"u_3 = \beta_3 = 3 = z", font_size=24
        ).next_to(step_text_u3, DOWN, buff=0.2)
        self.play(Write(u_3_result))
        self.wait(2)

        # Step Text for y calculation
        step_text_y = Text("Step 2: Compute y", font_size=24).next_to(u_3_result, DOWN, buff=0.2)
        self.play(Write(step_text_y))
        self.wait(1)

        # Directly display the equation for y
        y_result = MathTex(
            r"y = \beta_2 - \frac{c_2 \cdot u_3}{\alpha_2} = 2", font_size=24
        ).next_to(step_text_y, DOWN, buff=0.2)
        self.play(Write(y_result))
        self.wait(2)

        # Step Text for x calculation
        step_text_x = Text("Step 3: Compute x", font_size=24).next_to(y_result, DOWN, buff=0.2)
        self.play(Write(step_text_x))
        self.wait(1)

        # Directly display the equation for x
        x_result = MathTex(
            r"x = \beta_1 - \frac{c_1 \cdot u_2}{\alpha_1} = 1", font_size=24
        ).next_to(step_text_x, DOWN, buff=0.2)
        self.play(Write(x_result))
        self.wait(2)

        # Fade out all the formulas and texts
        self.play(FadeOut(coefficient_matrix), FadeOut(title), FadeOut(step_text_u3),
                  FadeOut(u_3_result), FadeOut(step_text_y), FadeOut(y_result), 
                  FadeOut(step_text_x), FadeOut(x_result))




class ThomasTridiagonalFinalScene(Scene):
    def construct(self):
        # Title for the final scene with smaller font size
        title = Text("Final Results - Thomas Tridiagonal System", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step Text: Present the original system of equations
        system_eq_text = Text("Original System of Equations", font_size=24).next_to(title, DOWN, buff=0.5)
        self.play(Write(system_eq_text))
        self.wait(1)

        # Display the system of equations
        eq1 = Text("4x - y = 2", font_size=24).next_to(system_eq_text, DOWN, buff=0.3)
        eq2 = Text("-x + 4y - z = 4", font_size=24).next_to(eq1, DOWN, buff=0.3)
        eq3 = Text("-y + 4z = 10", font_size=24).next_to(eq2, DOWN, buff=0.3)
        
        self.play(Write(eq1), Write(eq2), Write(eq3))
        self.wait(2)

        # Step Text: Mention the final solutions
        solution_text = Text("Final Solutions", font_size=24).next_to(eq3, DOWN, buff=0.5)
        self.play(Write(solution_text))
        self.wait(1)

        # Display the final solutions for x, y, z
        solution_x = Text(r"x = 1", font_size=24).next_to(solution_text, DOWN, buff=0.3)
        solution_y = Text(r"y = 2", font_size=24).next_to(solution_x, DOWN, buff=0.3)
        solution_z = Text(r"z = 3", font_size=24).next_to(solution_y, DOWN, buff=0.3)

        self.play(Write(solution_x), Write(solution_y), Write(solution_z))
        self.wait(2)

        # Fade out everything at the end
        self.play(FadeOut(title), FadeOut(system_eq_text), FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), 
                  FadeOut(solution_text), FadeOut(solution_x), FadeOut(solution_y), FadeOut(solution_z))

