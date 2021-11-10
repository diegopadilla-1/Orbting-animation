# Orbiting-animation
Simple python matplotlib code to animate orbits around a mass at the origin. Working on improvements to use exact equations of motion, add another "galaxy" and other objects and see how system evolves.

As for now 11/09/2021, the whole animation works using the constant acceleration formula for an acceleration computed using Newton's Law of Universal Gravitation. The first major improvement would be to compute the trajectory of each particle using Lagrangian mechanics to get an exact solution. 

The display of the animation itself is not my major concern, because the positions of each particle each frame could be easily exported to a file and then imported to a 3D animation software to produce a more pleasing looking video (Houdini could be an option), but before that I want to obtain a much more complex and accurate animation. 
