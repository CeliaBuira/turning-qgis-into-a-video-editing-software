# def main():
#     print("Hello from manimations!")

from pathlib import Path
from statistics import mean
from textwrap import wrap


from manim import *  # or: from manimlib import *
from manim_slides import Slide


import cv2
from PIL import Image, ImageOps
from dataclasses import dataclass

from shapely2manim import shapely2manim, manim2shapely, add_z

switzerland = [(0.13558678567707005, -0.840876415892391, 0.0), (0.3498905683745388, -0.9077257729589882, 0.0), (0.545869307705952, -0.6773114604149282, 0.0), (0.4963515795342057, -0.5572990112165771, 0.0), (0.7411917844181264, -0.35385647120307573, 0.0), (0.7485499129612723, -0.5721787217732678, 0.0), (0.8687788508848953, -0.6987005678713829, 0.0), (1.0411439384810985, -0.7452386582323132, 0.0), (0.9942923320141397, -0.8328984556294794, 0.0), (1.0684279618041215, -0.8605488514551825, 0.0), (1.084388809450501, -0.9879211957093679, 0.0), (1.1604091730437593, -1.0, 0.0), (1.2087328553413257, -0.9181872373267281, 0.0), (1.1355179791205892, -0.8467069571588757, 0.0), (1.149189629112965, -0.7793458543433696, 0.0), (1.3129848784627072, -0.5788727508952806, 0.0), (1.3305471477971094, -0.3104070847753815, 0.0), (1.4576021404069204, -0.2962719231712033, 0.0), (1.458887270580377, -0.42984648111356005, 0.0), (1.523629076481829, -0.5029874822561757, 0.0), (1.8070384764871386, -0.4176062203712303, 0.0), (1.8716079654187143, -0.5655546678985013, 0.0), (1.9431468261725597, -0.5626505755787274, 0.0), (1.9114338189632458, -0.45996891799884243, 0.0), (1.9511150918239277, -0.3825824028464333, 0.0), (1.8637611133876146, -0.3510534315371473, 0.0), (1.8627437289932693, -0.2482014841742336, 0.0), (1.995003847777388, -0.15072519892476532, 0.0), (2.037357325264104, -0.23542285776825977, 0.0), (2.15908638468286, -0.23897901160887447, 0.0), (2.1713129979696126, -0.1649107925188712, 0.0), (2.0916746210368107, -0.09803940111979403, 0.0), (2.1559307958068685, 0.1627889284134616, 0.0), (2.0598085908990003, 0.21227407266951137, 0.0), (1.8944406307334787, 0.053721224246115584, 0.0), (1.7332787042949476, 0.1441975322522402, 0.0), (1.7291642420818216, 0.2306194562901469, 0.0), (1.451449310666367, 0.2546713521065458, 0.0), (1.5662366312273672, 0.6635145385199819, 0.0), (1.2853484305341611, 0.8636274713566567, 0.0), (1.0398192095430034, 0.8483180611293684, 0.0), (0.9767204838125665, 0.938697771005675, 0.0), (0.9241678459760765, 0.8914557264787082, 0.0), (0.8734481977714343, 1.0, 0.0), (0.7027884848190213, 0.8940035205478396, 0.0), (0.8567674776044245, 0.8494421579934293, 0.0), (0.7287457374995521, 0.7625018087293711, 0.0), (0.5703245607007073, 0.8153083964581567, 0.0), (0.2189845299887585, 0.7225381630354357, 0.0), (0.1766777418712202, 0.7512617140750453, 0.0), (0.21749583893170787, 0.7916302812507123, 0.0), (0.14593241212986752, 0.7804925495789887, 0.0), (0.01799633166838821, 0.6241167663165221, 0.0), (-0.08835341214032566, 0.6087600202072534, 0.0), (-0.14108690482822728, 0.6333566616781308, 0.0), (-0.11971984823319981, 0.6844852107579937, 0.0), (-0.2567309134626701, 0.6897704559972906, 0.0), (-0.34112849731757977, 0.5426998050653375, 0.0), (-0.21964051088483116, 0.5225490014474359, 0.0), (-0.46196337973331714, 0.2311713316342754, 0.0), (-0.6535548238910238, 0.11480017573244772, 0.0), (-0.6431386556969684, -0.04071284349367843, 0.0), (-0.8842163412473449, -0.23785129158711005, 0.0), (-0.851916677132792, -0.2696820068998669, 0.0), (-0.9186650555251288, -0.39892857572412543, 0.0), (-0.8452437270881168, -0.4497672520829864, 0.0), (-1.0, -0.6845280854866078, 0.0), (-0.7598214441971978, -0.5946192203350245, 0.0), (-0.8117318911617954, -0.5061821342238602, 0.0), (-0.729554049973261, -0.414375033254309, 0.0), (-0.3893690820393574, -0.3944045206952339, 0.0), (-0.4246008968113023, -0.4698282668311461, 0.0), (-0.35971874958235317, -0.5437583928830514, 0.0), (-0.40787076261584765, -0.6885829956961671, 0.0), (-0.33623909145373887, -0.7016411113433287, 0.0), (-0.3560949413882871, -0.7752231548791583, 0.0), (-0.30958049936543963, -0.7632463789694783, 0.0), (-0.1954339200501949, -0.9703780759521684, 0.0), (0.13558678567707005, -0.840876415892391, 0.0)]


FREYA_BLUE = "#32bcfd"
FREYA_YELLOW = "#14fda5"
FREYA_RED = "#fc1153"
FREYA_GRAY = "#0e1a26"

def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * a + t * b

def normalize_v(v):
    #inspired from https://stackoverflow.com/questions/21030391/how-to-normalize-a-numpy-array-to-a-unit-vector
    norm = np.linalg.norm(v)
    if norm == 0: 
       raise ZeroDivisionError
    return v / norm

def to_circle_manim(geometry: Polygon, t: float=1) -> Polygon:
    centroid = geometry.get_center()
    
    vertices = [v for v in geometry.get_vertices()]
    
    distance_centroid_vertex = [Line(v, centroid).get_length() for v in vertices]


    average = goal = mean(distance_centroid_vertex)
    
    
    vectors = [ v - centroid for v in vertices]
    vectors = [normalize_v(vector) * lerp(original_dist, goal, t) for vector, original_dist in zip(vectors, distance_centroid_vertex)]
    
    end_vertices = [centroid + final_vector for final_vector in vectors]

    
    polygon = Polygon(*end_vertices) 
    return polygon

def my_code_step(code_string):
    code_step = Code(
            code_string=code_string,
            language="haskell",   # often better than "lisp"
            background="window",
            formatter_style='vim',
            # insert_line_no=False,
            # style="monokai",
            
        )
    code_step.scale(0.6).scale(0.5)
    code_step.to_edge(RIGHT)
    return code_step

@dataclass
class VideoStatus:
    time: float = 0
    videoObject: cv2.VideoCapture = None
    def __deepcopy__(self, memo):
        return self

class VideoMobject(ImageMobject):
    '''
    Following a discussion on Discord about animated GIF images.
    Modified for videos
    Parameters
    ----------
    filename
        the filename of the video file
    imageops
        (optional) possibility to include a PIL.ImageOps operation, e.g.
        PIL.ImageOps.mirror
    speed
        (optional) speed-up/slow-down the playback
    loop
        (optional) replay the video from the start in an endless loop
    https://discord.com/channels/581738731934056449/1126245755607339250/1126245755607339250
    2023-07-06 Uwe Zimmermann & Abulafia
    2024-03-09 Uwe Zimmermann
    '''
    def __init__(self, filename=None, imageops=None, speed=1.0, loop=False, **kwargs):
        self.filename = filename
        self.imageops = imageops
        self.speed    = speed
        self.loop     = loop
        self._id = id(self)
        self.status = VideoStatus()
        self.status.videoObject = cv2.VideoCapture(filename)

        self.status.videoObject.set(cv2.CAP_PROP_POS_FRAMES, 1)
        ret, frame = self.status.videoObject.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)            
            img = Image.fromarray(frame)

            if imageops != None:
                img = imageops(img)
        else:
            img = Image.fromarray(np.uint8([[63, 0, 0, 0],
                                        [0, 127, 0, 0],
                                        [0, 0, 191, 0],
                                        [0, 0, 0, 255]
                                        ]))
        super().__init__(img, **kwargs)
        if ret:
            self.add_updater(self.videoUpdater)

    def videoUpdater(self, mobj, dt):
        if dt == 0:
            return
        status = self.status
        status.time += 1000*dt*mobj.speed
        self.status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
        ret, frame = self.status.videoObject.read()
        if (ret == False) and self.loop:
            status.time = 0
            self.status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
            ret, frame = self.status.videoObject.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # needed here?        
            img = Image.fromarray(frame)

            if mobj.imageops != None:
                img = mobj.imageops(img)
            mobj.pixel_array = change_to_rgba_array(
                np.asarray(img), mobj.pixel_array_dtype
            )
    def duration(self):
        try:
            frame_count = int(self.status.videoObject.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = self.status.videoObject.get(cv2.CAP_PROP_FPS)
        except:
            raise(Exception("video Object not set"))

        duration_seconds = frame_count / fps
        return duration_seconds


SKIP_ANIMATIONS = True
SKIP_ANIMATIONS_INTRO = True
SKIP_ANIMATIONS_PART1 = True
SKIP_ANIMATIONS_PART2 = True
SKIP_ANIMATIONS_PART3 = True
config.background_color = FREYA_GRAY

"""
ALL SLIDE

* summary Done 
* to circle
    - loop
    - distance centroid vertex
    - interpolation lerp
    - put everything in a python expression and use in a geometry generator
* control t value
    - evolution chaque steps (simple t as a pct, only sin, add thin line, )
    - with variable
    - Show failure Done
    - Explain the workflow with video qgis/blender/Desmos Done could be improved
* Common goal (animate a line, point along a line,apparition, buffer )
* Common goal keyframing
* Push QGIS to the limit to highlight it's flaw( Eats your own dogs ):
    - eye for symbologie  funded by QGIS.ch, thanks you ! 
    - keyframe (Stoneage of the motion graphic software ) - add mockup
    - eventuellement list tool les problemes 
    - eventuellement lister toutes les choses faites
*what's next ? call for help
* le rab (freya etc..)
"""

class BasicExample(Slide):
    def construct(self):
        # circle = Circle(radius=3, color=BLUE)
        # dot = Dot()

        # self.play(GrowFromCenter(circle))


    
        intro_video = VideoMobject("./images/to_circle_intro_video.mp4")
        intro_video.scale(0.6).to_edge(LEFT)
        self.add(intro_video)

        intro_text = Text("1) Deform a geometry into circle\n\n\n" \
        "2) Control the deformation")
        intro_text.scale(0.5).to_edge(RIGHT)

        self.add(intro_text)

        self.wait(5)
        self.next_slide(skip_animations=SKIP_ANIMATIONS_INTRO)  

        self.clear()
        equal_sign = Text("=")
        equal_sign.scale(2.5)


        intro_expression_engine = ImageMobject("./images/intro expression.png")
        intro_kdenlive = ImageMobject("./images/kdenlive.png")

        intro_expression_engine.scale(0.8)
        intro_kdenlive.scale(0.7)

        intro_expression_engine.next_to(equal_sign, LEFT)
        intro_kdenlive.next_to(equal_sign, RIGHT)

        self.add(equal_sign, intro_expression_engine, intro_kdenlive)


        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1) 



        # self.next_slide(skip_animations=SKIP_ANIMATIONS)

        # self.play(dot.animate.move_to(RIGHT * 2))

        # video1 = VideoMobject(
        #     filename=r"/home/valentin/Videos/drag and drop no more switch source.mp4",
        #     speed=1.0
        # ).scale_to_fit_width(5).to_corner(UL)
        # video2 = VideoMobject(
        #     filename=r"/home/valentin/Videos/rail road to laax.mp4",
        #     speed=3.0,
        #     loop=True,
        #     imageops=ImageOps.mirror
        # ).scale_to_fit_width(5).to_corner(UR)


        # self.add(video1)
        # self.add(video2)

        # self.play(video1.animate.shift(3*DL), run_time=6)

        # self.remove(video1)
        # self.remove(video2)
        # self.next_slide(skip_animations=SKIP_ANIMATIONS)

        # text1 = Text("Hello")
        # text2 = Text("Goodbye", color=YELLOW)

        # self.play(Transform(text1, text2))
        # text2.to_edge(LEFT)
        # self.wait()
        # self.next_slide(skip_animations=False)

        self.clear()

        switzerland_p = Polygon(*switzerland)

        switzerland_p.scale(2)
        switzerland_p.to_edge(LEFT)


        self.add(switzerland_p)
        self.wait()

        self.next_slide(skip_animations = SKIP_ANIMATIONS_PART1)

        # centroid = manim2shapely(switzerland_p).centroid
        
        # switzerland_center = Dot((centroid.x, centroid.y, 0))
        # self.add(switzerland_center)


        

        end_circle = Circle()
        end_circle.scale(2)
        end_circle.to_edge(RIGHT)

        interrogation = Text("?")
        arrow_polygon_to_circle= Arrow(switzerland_p.get_right(), end_circle.get_left())
        interrogation.next_to(arrow_polygon_to_circle, UP)


        self.add(end_circle)
        self.add(arrow_polygon_to_circle)
        self.add(interrogation)

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)

        self.play(FadeOut(arrow_polygon_to_circle, end_circle, interrogation))
        

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)

        centroid_dot =  Dot(switzerland_p.get_center(), color=YELLOW)
        # self.add(centroid_dot)
        
        self.play(GrowFromCenter(centroid_dot))


        


        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)


        lines_grp = VGroup()
        offset = 15
        vertices = switzerland_p.get_vertices()
        
        lengths = []
        for i in range(len(vertices), 0, -1):
            vertex = vertices[(i+offset)%len(vertices)]
            l = Line(start=switzerland_p.get_center(), end=vertex, stroke_width=1)   
            lengths.append(l.get_length())
            lines_grp.add(l)
        
        # self.play(Create(lines_grp))



        if SKIP_ANIMATIONS:
            lengths = lengths[0:7]



        chart = BarChart(
            values=[0 for i in lengths],
            x_length=10,
            y_range= [0, max(lengths), 0.5],
            x_axis_config={"font_size": 36},
        )
        chart.scale(0.5)
        chart.to_edge(RIGHT)


        datasets = []
        for n in range(len(lengths)):
            v = [0 if i>n else lengths[i] for i in range(len(lengths))]
            datasets.append(v)

        chart_steps = []
        for dataset in datasets:
            chart_tmp = BarChart(
                values=dataset,
                x_length=10,
                y_range= [0, max(lengths), 0.5],
                x_axis_config={"font_size": 36},
            )
            chart_tmp.scale(0.5)
            chart_tmp.to_edge(RIGHT)
            chart_steps.append(chart_tmp)


        chart2 = BarChart(
            values=[1 for i in lengths],
            x_length=10,
            y_range= [0, max(lengths), 0.5],
            x_axis_config={"font_size": 36},
        )
        chart2.scale(0.5)
        chart2.to_edge(RIGHT)

        chart3 = BarChart(
            values=lengths,
            x_length=10,
            y_range= [0, max(lengths), 0.5],
            x_axis_config={"font_size": 36},
        )
        chart3.scale(0.5)
        chart3.to_edge(RIGHT)


        self.add(chart)

        run__time = 4
        self.play( 
            Create(lines_grp, run_time=run__time), 
            Succession(*[Transform(chart, c) for c in chart_steps ] , run_time=run__time))
        
        bar_animations = [
            chart.animate.change_bar_values(list(reversed(lengths))), 
            chart.animate.change_bar_values(lengths)
            ]

        self.wait()
        self.next_slide(loop=False, skip_animations=SKIP_ANIMATIONS)

        # self.clear()

        avg_length = mean( lengths )
        avg_circle = Circle(radius=avg_length).move_to(switzerland_p.get_center()).reverse_points()
        avg_circle.color = FREYA_YELLOW
        # avg_circle.rotate(PI/2)


        left = chart.c2p(0, avg_length)
        right = chart.c2p(len(lengths), avg_length)
        avg_line = Line(left, right)
        avg_line.color = FREYA_YELLOW
        self.play(Create(avg_line))


        # avg_line2 = Line(right, left )
        # avg_line2 = Line(left, right )
        avg_line2= ArcBetweenPoints(start=left, end=right, angle=0)
        avg_line.color = FREYA_YELLOW
        

        self.add( avg_line2 )
        self.play(Transform(avg_line2, avg_circle,
                            path_arc=PI/2,
                            #  path_arc_centers=lambda p0, p1: np.array([0, 0, 0])
                             ))
        
        self.add(avg_circle)

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)

        # LERP 
        self.remove(avg_line)
        self.remove(avg_line2)
        self.remove(chart)
        self.remove(lines_grp)
        

        title_lerp = MarkupText("<i><b>L</b></i>inear int<i><b>erp</b></i>olation aka Lerp")
        title_lerp.to_edge(UP)
        self.add(title_lerp)


        nb_line = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_ticks=True,
            # numbers_to_include=[-8, 8],
            include_numbers=False,
            font_size=24,
        )
        nb_line.get_tick(-8)
        nb_line.get_tick(4)

        nb_line.scale(0.5)
        nb_line.to_edge(RIGHT)

        a_nb = -8
        b_nb = 8
        a_point = Dot(nb_line.n2p(a_nb), color=FREYA_RED)
        b_point = Dot(nb_line.n2p(b_nb), color=FREYA_BLUE)
        

        equation = MathTex(r"lerp(a, b, t) = a + t * (b-a)",     tex_to_color_map={
        "a": FREYA_RED,
        "b": FREYA_BLUE,
        "t": FREYA_YELLOW
    })
        equation.next_to(nb_line, UP)


        self.add(equation)
        self.add(nb_line)
        self.play(Create(a_point), Create(b_point))

        t_tracker = ValueTracker(0)

        def t_text_callback():
            txt = MathTex(f"t={round(t_tracker.get_value(), 2)}")
            txt.set_color(FREYA_YELLOW)
            txt.next_to( nb_line.n2p( lerp( a_nb, b_nb, t_tracker.get_value() ) ), DOWN )
            return txt
        
        t_text = always_redraw(
            t_text_callback
        )
        t_dot = always_redraw(
            lambda: Dot(
                point= utils.bezier.interpolate(a_point.get_center(), b_point.get_center(), t_tracker.get_value()),
                color= core.interpolate_color(ManimColor(FREYA_RED), ManimColor(FREYA_BLUE), t_tracker.get_value() )
            )
        )


        def t_circle_callback():
            circ =  to_circle_manim(switzerland_p, t=t_tracker.get_value())
            col = core.interpolate_color(ManimColor(FREYA_RED), ManimColor(FREYA_BLUE), t_tracker.get_value() )
            dots = [Dot(v, radius=0.05, color=col) for v in circ.get_vertices() ]
            # dot
            dot_grp = VGroup(*dots[::2])

            circ.add(dot_grp)
            circ.set_color( color=col )
            return circ

        t_circle = always_redraw(
            t_circle_callback
        )

        # switzerland_to_circle = to_circle_manim(switzerland_p, 1)
        # self.add(switzerland_to_circle)
        
        end_circle = to_circle_manim(switzerland_p, 1)
        lines_start_to_end_circle =  [
                Line(start=start_vertice, end=end_vertices, stroke_width=1.2) for start_vertice, end_vertices in zip( end_circle.get_vertices(), switzerland_p.get_vertices() )
                ]
        lines_start_to_end_circle = VGroup(
            *lines_start_to_end_circle[::2]
            )
        
        self.add(t_text)
        self.add(t_dot)

        self.play(t_tracker.animate.set_value(1), run_time=3)
        self.play(t_tracker.animate.set_value(0), run_time=3)
        

        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)

        self.add(lines_start_to_end_circle)

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)

        self.add(t_circle)

        self.play(t_tracker.animate.set_value(1), run_time=3)

        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)


        self.play( t_tracker.animate.set_value(2) )




        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART1)

        self.clear()

        # title_geometry_generator =  Text("Put everything in an expression and use it in a geometry geneator")
        # self.add(title_geo    metry_generator)

        expression_to_generator1 = ImageMobject("./images/to_circle_qgis0.png").scale(0.8)
        expression_to_generator2 = ImageMobject("./images/to_circle_qgis1.png").scale(0.8)

        expression_to_generator1.to_edge(UP)
        expression_to_generator2.next_to(expression_to_generator1, DOWN)

        # expression_to_generator1.to_edge(LEFT)
        # expression_to_generator2.to_edge(RIGHT)

        self.add(expression_to_generator1, expression_to_generator2)


        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2)
        # self.clear()

        # python_string = """from manim import *
        # from manim_slides import Slide

        # class Example(Slide):
        #     def construct(self):
        #         dot = Dot()
        #         self.add(dot)

        #         self.play(Indicate(dot, scale_factor=2))
        #         self.next_slide()
        #         square = Square()
        #         self.play(Transform(dot, square))
        #         self.next_slide()
        #         self.play(Rotate(square, angle=PI/2))
        # """

        # code_python = Code(
        #     code_string=python_string,
        #     language="python",
        # )
        # self.add(code_python)

        # self.wait()
        # self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2)
        self.clear()

        video_timeline = VideoMobject(
            filename=r"./images/timeline.mp4",
            loop=True,
            # imageops=ImageOps.mirror
        ).scale_to_fit_width(5).to_corner(DL)
        self.add(video_timeline)

        expression_step1 = """with_variable('t',  (@frame_number+1) / @total_frame_count, 
	 to_circle( @geometry, @t )
)"""


        code_step_1 = Code(
            code_string=expression_step1,
            language="haskell",   # often better than "lisp"
            background="window",
            formatter_style='vim',
            # insert_line_no=False,
            # style="monokai",
            
        )
        code_step_1.scale(0.6)
        code_step_1.to_edge(RIGHT)

        self.add(code_step_1)

        explain_step_text = Text("'with_variable', assign a variable to resuse it later in an expression")
        explain_step_text.scale(0.6)
        explain_step_text.to_corner(DL)
        self.add(explain_step_text)

        self.wait( video_timeline.duration() )
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2, loop=True)

        expression_step_2 = """with_variable('frame_pct',  (@frame_number+1) / @total_frame_count, 
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( @dt_offset )
		, -1,1
		, 0,1.2
	 ),

	 to_circle( @geometry, @t )
	 --@frame_pct
)))        
"""
        c2 = my_code_step(expression_step_2)


        explain_step_2_text = Text("Follow a sin function")


        self.play(Transform(code_step_1, c2), 
                  Wait(video_timeline.duration()),
                  Transform(explain_step_text, explain_step_2_text)
                  )
        
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2)

        # =============
        # Step 2.1
        # =============

        expression_step_3 = """with_variable('scale_coord', 2 * PI() * 9,
with_variable('x_coord', inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), x($geometry) )* @scale_coord,
with_variable('frame_pct',  (@frame_number+1) / @total_frame_count, 
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( @dt_offset + @x_coord  )
		, -1,1
		, 0,1.2
	 ),

	 to_circle( @geometry, @t )
)))))"""
        c3 = my_code_step(expression_step_3)
        self.play(Transform(code_step_1, c3),
                  Wait(video_timeline.duration())
                  )
        
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2)

        expression_step_4 = """with_variable('scale_coord', 2 * PI() * 9,
with_variable('x_coord', inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), x($geometry) )* @scale_coord,
with_variable('y_coord', 
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), y($geometry) ) 
	* @scale_coord,

with_variable('frame_pct',  (@frame_number+1) / @total_frame_count, 
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( -@dt_offset + sqrt( (@x_coord)^2 + (@y_coord)^2))
		, -1,1
		, 0,1.2
	 ),

	 to_circle( @geometry, @t )
))))))"""

        c4 = my_code_step(expression_step_4)
        self.play(Transform(code_step_1, c4),
                  Wait(video_timeline.duration())
                  )
        
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2)

        expression_step_5 = """with_variable('scale_coord', 2 * PI() * 9,
with_variable('x_coord', 
    inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), x($geometry) ) 
	* @scale_coord,
with_variable('y_coord', 
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), y($geometry) ) 
	* @scale_coord,
with_variable('lebanon_x', 
    inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), -216962.970 ) 
	* @scale_coord,
with_variable('lebanon_y',
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), 1868583.826 ) 
	* @scale_coord,
with_variable('frame_pct',  (@frame_number+1) / @total_frame_count, 
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( -@dt_offset + sqrt( (@x_coord-@lebanon_x)^2 + (@y_coord-@lebanon_y)^2))
		, -1,1
		, 0,1
	 ),
	
	 to_circle( @geometry, @t )
))))))))


"""

        c5 = my_code_step(expression_step_5)
        self.play(Transform(code_step_1, c5),
                  Wait(video_timeline.duration())
                  )
        
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART2)
        

        print("animation around ~")

        expression_step_6 = """with_variable('scale_coord', 2 * PI() * 9,
with_variable('normalize_scale',
    (maximum( x_max( $geometry) ) - minimum( x_min( $geometry) )) 
	/ (maximum( y_max( $geometry)) - minimum( y_min( $geometry) )) ,
with_variable('x_coord', 
    inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), x($geometry) ) 
	* @scale_coord,
with_variable('y_coord', 
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), y($geometry) ) 
	* @scale_coord / @normalize_scale,
with_variable('lebanon_x', 
    inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), -216962.970 ) 
	* @scale_coord,
with_variable('lebanon_y',
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), 1868583.826 ) 
	* @scale_coord / @normalize_scale,
with_variable('frame_pct',  (@frame_number+1) / @total_frame_count, 
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( -@dt_offset + sqrt( (@x_coord-@lebanon_x)^2 + (@y_coord-@lebanon_y)^2))
		, -1,1
		, 0,1
	 ),
	
	 to_circle( @geometry, @t )

)))))))))"""

        


        # expression_step_6 = "\n".join(wrap(expression_step_6))
        code_step_6 = Code(
            code_string=expression_step_6,
            language="haskell",   # often better than "lisp"
            background="window",
            formatter_style='vim',
            # insert_line_no=False,
            # style="monokai",
            
        )
        # code_step_6.remove(code_step_6.background)
        code_step_6.scale(0.6).scale(0.5)
        code_step_6.to_edge(RIGHT)

        # self.add(code_step_6)
        self.play(Transform(code_step_1, code_step_6), 
                  Wait(video_timeline.duration())
                  )
        #maybe use? #TransformMatchingShapes


        self.next_slide(skip_animations=SKIP_ANIMATIONS)



        self.clear()

        my_workflow_text = Text("My workflow")
        my_workflow_text.to_edge(UP)


        target_image_height = 1

        # blender_text = Text("Blender")
        # blender_logo = SVGMobject("./images/logos/blender_logo.svg")

        
        blender_logo = ImageMobject("./images/logos/blender_logo.png").set_height(target_image_height)
        blender_screenshot = ImageMobject("./images/workflow/blender_screenshot.png")
        blender_screenshot.scale_to_fit_width(blender_logo.width)
        blender_screenshot.next_to(blender_logo, direction=UP)
        blender_grp = Group(blender_screenshot, blender_logo)

        self.add(blender_grp)
        blender_grp.to_corner(UL)
        
        # desmos_logo = SVGMobject("./images/logos/desmos_logo.svg")
        desmos_logo = ImageMobject("./images/logos/desmos_logo.png").set_height(target_image_height)
        desmos_screenshot = ImageMobject("./images/workflow/desmos_screenshot.png")
        desmos_screenshot.scale_to_fit_width(desmos_logo.width)
        desmos_screenshot.next_to(desmos_logo, direction=UP)
        desmos_grp = Group(desmos_screenshot, desmos_logo)

        self.add(desmos_grp)
        desmos_grp.to_corner(UR)



        # qgis_logo = SVGMobject("./images/logos/qgis_logo.svg")
        qgis_logo = ImageMobject("./images/logos/qgis_logo.png").set_height(target_image_height).scale(1.1)
        
        
        qgis_screenshot1 = ImageMobject("./images/workflow/qgis_screenshot1.png")
        qgis_screenshot2 = ImageMobject("./images/workflow/qgis_screenshot2.png")


        qgis_screenshot1.scale_to_fit_width(qgis_logo.width/2).scale(2)
        qgis_screenshot2.scale_to_fit_width(qgis_logo.width/2).scale(2)
        
        qgis_screenshot2.next_to(qgis_screenshot1)

        qgis_screenshot_grp = Group(qgis_screenshot1, qgis_screenshot2)

        qgis_screenshot_grp.next_to(qgis_logo, direction=UP)


        

        qgis_grp = Group(qgis_screenshot_grp, qgis_logo)

        self.add(qgis_grp)
        qgis_grp.to_edge(DOWN)
        
        # Arrow()

        a1 = Arrow(start=blender_grp.get_bottom(), end=qgis_grp.get_left())
        a2 = Arrow(start=desmos_grp.get_bottom(), end=qgis_grp.get_right())
        a3 = DoubleArrow(start=blender_grp.get_right(), end=desmos_grp.get_left())

        self.add(my_workflow_text)
        self.add(a1,a2,a3)
        

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS)

        self.clear()


        failed1 = ImageMobject("./images/failed_attempt/failed_screenshot.png")
        failed2 = ImageMobject("./images/failed_attempt/failed2.png")

        failed1.scale_to_fit_width(config.frame_width / 2 * 0.95)
        failed2.scale_to_fit_width(config.frame_width / 2 * 0.95)

        failed1.to_edge(LEFT, buff=0.2)
        failed2.to_edge(RIGHT, buff=0.2)

        self.add(failed1, failed2)

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS)

        self.clear()

        common_goal_exemple_text = Text("Frequent use case: animate a line")
        common_goal_exemple_text.to_edge(UP)

        line_animation = VideoMobject("./images/exemples/line.mp4").scale(0.8)
        line_animation.to_edge(LEFT)
        self.add(line_animation)

        line_animation_tuto1 = ImageMobject("./images/exemples/line_simple_tuto0.png")
        line_animation_tuto2 = ImageMobject("./images/exemples/line_simple_tuto1.png")
        line_animation_tuto3 = ImageMobject("./images/exemples/line_simple_tuto2.png")

        line_animation_tuto1.next_to(common_goal_exemple_text, DOWN)
        line_animation_tuto1.to_edge(RIGHT)
        line_animation_tuto2.next_to(line_animation_tuto1, DOWN)
        line_animation_tuto2.align_to(line_animation_tuto1, LEFT)
        line_animation_tuto3.next_to(line_animation_tuto2, DOWN)
        line_animation_tuto3.align_to(line_animation_tuto1, LEFT)


        self.add(line_animation_tuto1)
        self.add(line_animation_tuto2)
        self.add(line_animation_tuto3)

        self.add(common_goal_exemple_text)

        

        self.wait( line_animation.duration() )
        self.next_slide(skip_animations=SKIP_ANIMATIONS)
        self.clear()


        frequent_use_case_buffer = Text("Frequent use case: \nAnimate a buffer expanding")
        frequent_use_case_buffer.to_edge(UP)
        

        buffer_animation = VideoMobject("./images/exemples/buffer_expanding.mp4").scale(0.8)
        buffer_animation.to_edge(LEFT)
        self.add(buffer_animation)

        buffer_animation_tuto1 = ImageMobject("./images/exemples/buffer_simple_tuto1.png")
        buffer_animation_tuto2 = ImageMobject("./images/exemples/buffer_simple_tuto2.png")

        buffer_animation_tuto1.next_to(frequent_use_case_buffer, DOWN)
        buffer_animation_tuto1.to_edge(RIGHT)
        buffer_animation_tuto2.next_to(buffer_animation_tuto1, DOWN)
        buffer_animation_tuto2.align_to(buffer_animation_tuto1, LEFT)

        self.add(buffer_animation_tuto1)
        self.add(buffer_animation_tuto2)

        self.add(frequent_use_case_buffer)

        

        self.wait( buffer_animation.duration() )



        # animate a line -> rail to laax
        # animate a point line -> memoire ou skip ?
        # animate apparition -> memoire / opacity
        # animate a buffer expanding 



        #And of course you can combine then together



        self.next_slide(skip_animations=False)

        self.clear()


        common_goal_keyframe = Text("One step further: keyframing")
        self.add(common_goal_keyframe)
        common_goal_keyframe.to_edge(UP)

        keyframe_animation = VideoMobject("./images/exemples/buffer_keyframe.mp4").scale(0.6)
        keyframe_animation.to_edge(LEFT)
        self.add(keyframe_animation)

        keyframing_img = ImageMobject("./images/keyframing/keyframing_illus.jpeg").scale(1.5)
        keyframing_img.to_edge(RIGHT)
        self.add(keyframing_img)

        self.wait(keyframe_animation.duration())
        self.next_slide(skip_animations=False)

        self.remove(keyframing_img)



        keyframe_expression = """with_variable('keyframe_1', 50, /* a frame */ 
with_variable('keyframe_2', 150, /* a frame */
with_variable('keyframe_3', 250, /* a frame */
with_variable('keyframed_value',
CASE 
WHEN  @frame_number < @keyframe_1 THEN  
	10000 --meters
WHEN  @frame_number < @keyframe_2 THEN  
   lerp(10000, 20000, inverse_lerp(@keyframe_1,  @keyframe_2, @frame_number ) )  -- meters
WHEN  @frame_number < @keyframe_3 THEN  	
   lerp(20000, 10000, inverse_lerp(@keyframe_2,  @keyframe_3, @frame_number ) ) --meters
ELSE 100 --meters and final value
END,

buffer(@geometry, @keyframed_value)

))))
"""
        keyframe_code = my_code_step(keyframe_expression)

        instructions ="""
1. Define the keyframes 
2. Inverse lerp, to figure at which completion we are in between keyframe
3. Interpolate back between the value wanted at each keyframe by the 
""" 
        t = Text(instructions)
        self.add(t)

        self.add(keyframe_code)
        
        #Define the keyframes
        #  
        # 
        # Apply back the actual value using 

        # self.add(keyframe_code.code_lines[2])

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS_PART3)
        # self.remove(common_goal_keyframe)
        self.clear()

        funded_by_img = ImageMobject("./images/eyelid_funded.png")

        funded_by_coming_up = Text("QoL coming later this year")
        funded_by_coming_up.to_edge(UP)

        funded_by_text = Text("funded by")
        funded_by_text.next_to(funded_by_img, DOWN)

        
        qgis_ch_logo = ImageMobject("./images/qgis_ch_logo.png")
        qgis_ch_logo.next_to(funded_by_text)
        funded_by_thanks_text = Text("Thanks you!!")
        funded_by_thanks_text.next_to(qgis_ch_logo, DOWN)
        funded_by_thanks_text.align_to(funded_by_text, LEFT)

        
        self.add(funded_by_img)
        self.add(funded_by_coming_up)
        
        self.add(funded_by_text)
        self.add(qgis_ch_logo)
        self.add(funded_by_thanks_text)

        self.wait()
        self.next_slide(skip_animations=False)

        self.clear()

        video_editor_mockup = Text("mockup video editor / timeline/ keyframe ")
        self.add(video_editor_mockup)

        self.wait()
        self.next_slide(skip_animations=SKIP_ANIMATIONS)

        self.clear()
        whatsnext_text = Text("what's next ? I need your help\n if you know any of:").to_edge(UP)
        self.add(whatsnext_text)

        
        presse_img_grp = Group()
        presse_path = Path("./images/presse")
        for f in presse_path.iterdir():
            if f.suffix.lower() in [".png", ".jpg"]:
                g = Group()
                img = ImageMobject(f.absolute()).scale_to_fit_height(0.8)
                rect = RoundedRectangle(corner_radius=0.005, width=img.width, height=img.height, stroke_width=0)
                rect.set_fill(WHITE)
                rect.set_opacity(1)
                

                g.add(rect)
                g.add(img)

                print(f.absolute())
                presse_img_grp.add( g ) 




        presse_img_grp.arrange_in_grid(rows=4, cols=4,  buff=0.20).scale(0.8)
        presse_img_grp.next_to(whatsnext_text, DOWN)

        # and_so_on_text = Text("And so on ...")
        # and_so_on_text.next_to(presse_img_grp, direction=DOWN,  aligned_edge=RIGHT)
        # self.add(and_so_on_text)
        
        # p = f.absolute()
        # print(p)
        # img = ImageMobject(f.absolute())
        self.add(presse_img_grp)
        # self.play(Create(presse_img_grp))
        # for img in presse_img_grp:
        #     self.add(img)
        #     self.wait(0.2)

        # self.play(Add(presse_img_grp),run_time=2)
        # self.play(LaggedStart([Add(img, run_time=0.5) for img in presse_img_grp], lag_ratio=0.5) )
        
        
        contacts_me = Text("Contact me at:")
        contacts_me.next_to(presse_img_grp, DOWN)
        # contacts_me.align_to(whatsnext_text, LEFT)
        self.add(contacts_me)
        
        contacts = VGroup()
        contacts.add(Text("valentin@opengis.ch"))
        contacts.add(Text("valentin.buira@gmail.com"))
        contacts.add(Text("Valentin Buira on Linkedin"))
        contacts.add(Text("@cbuira.xyz on tiktok/instagram"))

        contacts.arrange(direction=DOWN, aligned_edge=LEFT)
        contacts.next_to(contacts_me, DOWN)
        contacts.scale(0.6)

        self.add(contacts)

        # self.add(presse_img_grp)

        # self.play(Create(presse_img_grp))


        # valentin@opengis.ch

        # Valentin Buira Linkedin
        # valentin.buira@gmail.com -> legacy
        # cbuira.xyz mastodon/tiktok/instagram

        self.wait()
        self.next_slide(skip_animations=False)
        # Group(Text("3Blue1Brown"))

        # self.wait()
        # self.next_slide(skip_animations=False)



# if __name__ == "__main__":
#     main()



# from manim import *


# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen