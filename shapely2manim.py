import shapely
from shapely import plotting
from matplotlib import pyplot as plt

from manim import *
from pyproj import Transformer
import numpy as np
from statistics import mean



def clamp01(t: float) -> float:
    return min(max(t, 0.0), 1.0)

def inverse_lerp(a: float, b: float, t: float)->float:
    return clamp01((t - a) / (b - a))

def lerp(a: float, b: float, t: float) -> float:
    """
    Linear interpolate on the scale given by a to b, using t as the point on that scale.
    """
    t = clamp01(t)
    return (1.0 - t) * a + t * b

def lerp_unclamped(a: float, b: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * a + t * b

def remap(value, start1, stop1, start2, stop2):
    """
    <h4>Syntax</h4>
    <p><b>remap</b>( value, start1, stop1, start2, stop2 )</p>
    """
    t = inverse_lerp(start1, stop1, value)
    #return t
    return start2 + (stop2 - start2) * t



g = shapely.from_geojson(open("switzerland.geojson").read())
g = g.simplify(0.05, preserve_topology=False)
g = g.geoms[0]



transformer = Transformer.from_crs(4326, 2056, always_xy=True)
g = shapely.transform(g, transformer.transform, interleaved=False)

(minx, miny, maxx, maxy) = g.bounds

x_range = maxx - minx
y_range = maxy - miny
ratio_x_range_by_y_range = x_range/y_range

def rerange(start, stop, multiplicator):
    return (start, start + (stop - start ) * multiplicator)
    


#maxx -> UP
#minx -> DOWN

(target_minx, target_maxx) = rerange(-1, 1, ratio_x_range_by_y_range)
vec = np.vectorize(lambda x, y: ( remap(x, minx, maxx, target_minx, target_maxx), remap(y, miny, maxy, -1, 1) )  )
g = shapely.transform( g, vec ,  interleaved=False)


plotting.plot_polygon(g)
vertices_3d = [(x, y, 0.0) for x, y in g.exterior.coords]
print(vertices_3d)
p = Polygon(*vertices_3d) 


def manim2shapely(polygon:Polygon) -> shapely.geometry:
    return shapely.Polygon(polygon.get_vertices())
    #return Polygon(*vertices_3d) 

def shapely2manim(geometry: shapely.Geometry)-> Polygon:
    vertices_3d = [(x, y, 0.0) for x, y in geometry.exterior.coords]
    return Polygon(*vertices_3d)


def add_z(point2d):
    return np.array([*point2d, 0.0])

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

def to_circle(geometry: Polygon, t: float=1):
    centroid = geometry.get_center()
    
    vertices = [v for v in geometry.get_vertices()]
    
    distance_centroid_vertex = [Line(v, centroid).get_length() for v in vertices]


    average = goal = mean(distance_centroid_vertex)
    
    
    vectors = [ v - centroid for v in vertices]
    vectors = [normalize_v(vector) * lerp(original_dist, goal, t) for vector, original_dist in zip(vectors, distance_centroid_vertex)]
    
    end_vertices = [centroid + final_vector for final_vector in vectors]

    
    polygon = Polygon(*end_vertices) 
    return polygon


circle = to_circle(p, 1)


class SimpleScene(Scene):
    def construct(self):
        self.add(p)
        self.wait()

        t = 1

        geometry = p
        centroid = geometry.get_center()

        self.add(Dot(centroid))
        self.wait()
    
        vertices = [v for v in geometry.get_vertices()]
        # vertices_as_geom = [QgsGeometry(v) for v in geometry.vertices()]

        for v in vertices:
            self.add(Dot(v))

        self.wait()
        
        distance_centroid_vertex = [Line(v, centroid).get_length() for v in vertices]

        average = goal = mean(distance_centroid_vertex)
        
        
        vectors = [ v - centroid for v in vertices]

        # for vector in vectors:
        #     v = Vector(direction=vector)
        #     v.shift(centroid)
        #     self.add(v)
        # self.wait()
        

        # import code
        # code.interact(local=dict(globals(), **locals()))
        
        #vectors = [vector.normalized() * lerp(original_dist, goal, t) for vector, original_dist in zip(vectors, distance_centroid_vertex)]
        vectors = [normalize_v(vector) * lerp(original_dist, goal, t) for vector, original_dist in zip(vectors, distance_centroid_vertex)]

        for vector in vectors:
            v = Vector(direction=vector)
            v.shift(centroid)
            self.add(v)
        self.wait()

        # vectors = [ np.array([vector.x(), vector.y(), vector.z()]) for vector in vectors]
        
        end_vertices = [centroid + final_vector for final_vector in vectors]
        #                #Point3DLike  #QVector3D

        
        polygon = Polygon(*end_vertices) 
        # self.add(polygon)
        self.add(to_circle(p))
        self.wait()




