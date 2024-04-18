from shapely.geometry import Polygon

# Define la función para crear un polígono cuadrado alrededor de un punto
def pointtopoly(punto,res=10):
    x, y = punto.x, punto.y
    return Polygon([(x-res/2, y-res/2), (x+res/2, y-res/2), (x+res/2, y+res/2), (x-res/2, y+res/2)])

# Crea una lista de polígonos cuadrados alrededor de cada punto de la grilla de puntos
grid_poligonos = [pointtopoly(punto) for punto in predictions['geometry']]

# Crea un nuevo GeoDataFrame con los polígonos y las predicciones asociadas a cada punto
grid_predicciones = gpd.GeoDataFrame({'geometry': grid_poligonos, 'pred': predictions['pred']})

        
"""         # Crea una lista para almacenar los puntos de la grilla
        grid_points = []
        # Itera sobre cada coordenada en la grilla
        for x in x_coords:
            for y in y_coords:
                # Crea un punto con las coordenadas actuales
                point = Point(x + grid_res/2, y + grid_res/2)  # Usa el punto central de cada celda
                
                # Agrega el punto a la lista
                grid_points.append(point) """

# Crea una grilla de celdas con la resolucion especificada en grid_res dentro del área del polígono
minx, miny, maxx, maxy = bound_grid.total_bounds
x_coords = range(int(minx), int(maxx), grid_res)
y_coords = range(int(miny), int(maxy), grid_res)
grid_cells = []
for x in x_coords:
    for y in y_coords:
        cell = Polygon([(x, y), (x + grid_res, y), (x + grid_res, y + grid_res), (x, y + grid_res)])
        grid_cells.append(cell)

grid = gpd.GeoDataFrame(geometry=grid_cells)

# Reproyecta la geometría de la grilla para que coincida con el CRS del perímetro
grid = grid.set_crs(bound_grid.crs)

# Intersecta la grilla con el polígono para eliminar las celdas que están fuera del perímetro
intersect_grid = gpd.overlay(grid, bound_grid, how='intersection')

# Obtenemos los vecinos mas cercanos de cada celda
grid = get_nearest_neighbors(gdf_obs=intersect_grid, gdf_cand=gdf, k_neighbors=knn)

legend_elements = [Line2D([0], [0], marker='s', color='w', label='0-10', markerfacecolor='#FF4500', markersize=10),
                   Line2D([0], [0], marker='s', color='w', label='10-15', markerfacecolor='#FFA500', markersize=10),
                   Line2D([0], [0], marker='s', color='w', label='15-20', markerfacecolor='#FFFF00', markersize=10),
                   Line2D([0], [0], marker='s', color='w', label='20-25', markerfacecolor='#7FFF00', markersize=10),
                   Line2D([0], [0], marker='s', color='w', label='25-30', markerfacecolor='#00FF00', markersize=10)]

from shapely.geometry import Polygon

# Define la función para crear un polígono cuadrado alrededor de un punto
def pointtopoly(punto,res=10):
    x, y = punto.x, punto.y
    return Polygon([(x-res/2, y-res/2), (x+res/2, y-res/2), (x+res/2, y+res/2), (x-res/2, y+res/2)])

# Crea una lista de polígonos cuadrados alrededor de cada punto de la grilla de puntos
grid_poligonos = [pointtopoly(punto) for punto in predictions['geometry']]

# Crea un nuevo GeoDataFrame con los polígonos y las predicciones asociadas a cada punto
grid_predicciones = gpd.GeoDataFrame({'geometry': grid_poligonos, 'pred': predictions['pred']})