from vector import Vector

class Ball:
    """ Maintains ball objects which can calculate their own movements

    A Ball object must be initialized with three vectors for the pos, vel, and
    acc attributes.

    >>> b = Ball(pos=Vector(0, 2), vel=Vector(5, 1), acc=Vector(1, -2))
    >>> b.pos
    Vector(x=0, y=2)
    >>> b.vel
    Vector(x=5, y=1)
    >>> b.acc
    Vector(x=1, y=-2)

    The string representation of a Ball object provides the current values of
    the pos, vel, and acc attributes.
    >>> b
    Ball(pos=Vector(x=0, y=2), vel=Vector(x=5, y=1), acc=Vector(x=1, y=-2))

    The update method updates the pos and vel attributes to the values after
    the specified duration has passed.  The acc vector must not be affected by
    each update.  Here, the x and y attributes in the pos and vel vectors are
    printed out directly with two decimal places to get around floating-point
    errors.
    >>> b.update(0.5) # update b to the next 0.5 second
    >>> f"pos=({b.pos.x:.2f},{b.pos.y:.2f}), vel=({b.vel.x:.2f},{b.vel.y:.2f})"
    'pos=(2.75,2.00), vel=(5.50,0.00)'
    >>> f"acc=({b.acc.x:.2f},{b.acc.y:.2f})"
    'acc=(1.00,-2.00)'
    >>> b.update(0.5) # update b to the next 0.5 second
    >>> f"pos=({b.pos.x:.2f},{b.pos.y:.2f}), vel=({b.vel.x:.2f},{b.vel.y:.2f})"
    'pos=(5.75,1.50), vel=(6.00,-1.00)'
    >>> f"acc=({b.acc.x:.2f},{b.acc.y:.2f})"
    'acc=(1.00,-2.00)'
    >>> b.update(0.1) # update b to the next 0.1 second
    >>> f"pos=({b.pos.x:.2f},{b.pos.y:.2f}), vel=({b.vel.x:.2f},{b.vel.y:.2f})"
    'pos=(6.36,1.38), vel=(6.10,-1.20)'
    >>> f"acc=({b.acc.x:.2f},{b.acc.y:.2f})"
    'acc=(1.00,-2.00)'

    """
    def __init__(self, pos, vel, acc):
        ''' Determine the initial position, velocity and acceleration of the ball as vector.

        :param pos: class
        :param vel: class
        :param acc: class
        '''
        self.pos = pos
        self.vel = vel
        self.acc = acc
    

    def update(self, dt):
        ''' Calculate new velocity and new position of the ball.

        :param dt: float
        '''
        self.vel = self.vel.add((self.acc.multiply(dt)))
        self.pos = self.pos.add((self.vel.multiply(dt)))
    

    def __repr__(self):
        ''' Display the ball instances

        '''
        return f"Ball(pos={self.pos}, vel={self.vel}, acc={self.acc})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()