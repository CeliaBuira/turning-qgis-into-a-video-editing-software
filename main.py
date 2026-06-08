# def main():
#     print("Hello from manimations!")

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

SKIP_ANIMATIONS = True

"""
ALL SLIDE

* summary
* to circle
* control t value
    - evolution chaque steps
* Common goal (animate a line, point along a line, )
*what's next ? call for help
* le rab (freya etc..)

    
"""

class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide(skip_animations=SKIP_ANIMATIONS)  # Waits user to press continue to go to the next slide

        # self.next_slide(loop=True)  # Start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide(skip_animations=SKIP_ANIMATIONS)  # This will start a new non-looping slide

        self.play(dot.animate.move_to(ORIGIN))

        
        self.next_slide(skip_animations=SKIP_ANIMATIONS)

        

        self.play(dot.animate.move_to(LEFT * 2))

        self.next_slide(skip_animations=SKIP_ANIMATIONS)

        self.play(dot.animate.move_to(RIGHT * 2))

        video1 = VideoMobject(
            filename=r"/home/valentin/Videos/drag and drop no more switch source.mp4",
            speed=1.0
        ).scale_to_fit_width(5).to_corner(UL)
        video2 = VideoMobject(
            filename=r"/home/valentin/Videos/rail road to laax.mp4",
            speed=3.0,
            loop=True,
            imageops=ImageOps.mirror
        ).scale_to_fit_width(5).to_corner(UR)


        self.add(video1)
        self.add(video2)

        self.play(video1.animate.shift(3*DL), run_time=6)

        self.remove(video1)
        self.remove(video2)
        self.next_slide(skip_animations=SKIP_ANIMATIONS)

        text1 = Text("Hello")
        text2 = Text("Goodbye", color=YELLOW)

        self.play(Transform(text1, text2))
        text2.to_edge(LEFT)
        self.wait()


        self.next_slide(skip_animations=False)

        self.clear()

        switzerland_p = Polygon(*switzerland)
        self.add(switzerland_p)

        switzerland_p.scale(2)
        switzerland_p.to_edge(LEFT)



        centroid = manim2shapely(switzerland_p).centroid
        
        switzerland_center = Dot((centroid.x, centroid.y, 0))
        self.add(switzerland_center)

        centroid_dot =  Dot(switzerland_p.get_center_of_mass(), color=YELLOW)
        self.add(centroid_dot)

        # c = Circle(radius=4)
        # self.add(c)

        self.wait()

        
        self.next_slide(skip_animations=SKIP_ANIMATIONS)


        lines_grp = VGroup()
        offset = 15
        vertices = switzerland_p.get_vertices()
        
        lengths = []
        for i in range(len(vertices), 0, -1):
            vertex = vertices[(i+offset)%len(vertices)]
            l = Line(start=switzerland_p.get_center(), end=vertex)   
            lengths.append(l.get_length())
            lines_grp.add(l)
        
        # self.play(Create(lines_grp))



        # if SKIP_ANIMATIONS:
        #     lengths = lengths[0:7]



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
        self.next_slide(loop=False)

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
        self.remove(avg_line2)
        self.add(avg_circle)
        self.wait()
        





        self.next_slide()

        # LERP 

        self.remove(chart)
        self.remove(lines_grp)
        self.wait()


        expression_string ="""with_variable('scale_coord', 2 * PI() * 9,
with_variable('normalize_scale',
    (maximum( x_max( $geometry) ) - minimum( x_min( $geometry) )) / (maximum( y_max( $geometry)) - minimum( y_min( $geometry) )) ,
with_variable('x_coord', 
    inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), x($geometry) ) * @scale_coord,
with_variable('y_coord', 
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), y($geometry) ) * @scale_coord / @normalize_scale,
with_variable('lebanon_x', 
    inverse_lerp( minimum( x_min( $geometry) ) , maximum( x_max( $geometry) ), -216962.970 ) * @scale_coord,
with_variable('lebanon_y',
    inverse_lerp( minimum( y_min( $geometry) ) , maximum( y_max( $geometry)), 1868583.826 ) * @scale_coord / @normalize_scale,
with_variable('frame_pct',  (@frame_number+1) / @total_frame_count, 
with_variable('keyframe_1', 150,
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( -@dt_offset + sqrt( (@x_coord-@lebanon_x)^2 + (@y_coord-@lebanon_y)^2))
		, -1,1
		, 0,1
	 ),
	
	 to_circle( @geometry, @t )

))))))))))"""

        python_string = """from manim import *
        from manim_slides import Slide

        class Example(Slide):
            def construct(self):
                dot = Dot()
                self.add(dot)

                self.play(Indicate(dot, scale_factor=2))
                self.next_slide()
                square = Square()
                self.play(Transform(dot, square))
                self.next_slide()
                self.play(Rotate(square, angle=PI/2))
        """

        code_step_3 = Code(
            code_string=python_string,
            language="python",
        )
        self.add(code_step_3)

        self.wait()
        self.next_slide()


        expression_string = """with_variable('scale_coord', 2 * PI() * 9,
with_variable('normalize_scale',
  (maximum(x_max($geometry)) - minimum(x_min($geometry))) /
  (maximum(y_max($geometry)) - minimum(y_min($geometry))),
with_variable('x_coord',
  inverse_lerp(
    minimum(x_min($geometry)),
    maximum(x_max($geometry)),
    x($geometry)
  ) * @scale_coord,
with_variable('y_coord',
  inverse_lerp(
    minimum(y_min($geometry)),
    maximum(y_max($geometry)),
    y($geometry)
  ) * @scale_coord / @normalize_scale,
with_variable('lebanon_x',
  inverse_lerp(
    minimum(x_min($geometry)),
    maximum(x_max($geometry)),
    -216962.970
  ) * @scale_coord,
with_variable('lebanon_y',
  inverse_lerp(
    minimum(y_min($geometry)),
    maximum(y_max($geometry)),
    1868583.826
  ) * @scale_coord / @normalize_scale,
with_variable('frame_pct',
  (@frame_number + 1) / @total_frame_count,
with_variable('keyframe_1', 150,
with_variable('dt_offset',
  @frame_pct * 2 * PI() * 9,
with_variable('t',
  scale_linear(
    sin(
      -@dt_offset +
      sqrt(
        (@x_coord - @lebanon_x)^2 +
        (@y_coord - @lebanon_y)^2
      )
    ),
    -1, 1,
     0, 1
  ),
  to_circle(@geometry, @t)
)))))))))"""

        expression_string = """with_variable('scale_coord', 2 * PI() * 9,
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
with_variable('keyframe_1', 150,
with_variable('dt_offset', @frame_pct *2 * PI() * 9,
with_variable('t', 
	scale_linear(
		sin( -@dt_offset + sqrt( (@x_coord-@lebanon_x)^2 + (@y_coord-@lebanon_y)^2))
		, -1,1
		, 0,1
	 ),
	
	 to_circle( @geometry, @t )

))))))))))"""
        self.wait()
        # self.next_slide(skip_animations=False)

        # expression_string = "\n".join(wrap(expression_string))
        code_step_4 = Code(
            code_string=expression_string,
            language="haskell",   # often better than "lisp"
            background="window",
            formatter_style='vim',
            # insert_line_no=False,
            # style="monokai",
            
        )
        # code_step_4.remove(code_step_4.background)
        code_step_4.scale(0.6)
        code_step_4.to_edge(RIGHT)

        self.add(code_step_4)

        self.wait()
        self.next_slide(skip_animations=False)
        self.wait()


        self.clear()
        text = Text("what's next ?")
        self.add(text)

        self.wait()
        self.next_slide(skip_animations=False)


# if __name__ == "__main__":
#     main()



# from manim import *


# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen