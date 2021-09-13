package src.hw3;

public class Bird {

    // 2 Shared fields that all other classes have
    private String name;
    private int age;

    // 1 unique field to the class
    private double flightHeight;

    public Bird(String name, int age, double flightHeight)
    {
        this.name = name;
        this.age = age;
        this.flightHeight = flightHeight;
    }

    /**
     * speak()
     * 
     * Generic speak method for speaking on its own
     */
    public void speak()
    {
        System.out.println(this.name + " the bird says Chirp Chirp");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to cats
     * @param c
     */
    public void speak(Cat c)
    {
        System.out.println(this.name + " the bird says Chirp Chirp to " + c.getName() + " the cat.");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to other birds
     * @param b
     */
    public void speak(Bird b)
    {
        System.out.println(this.name + " the bird says Chirp Chirp to " + b.getName() + " the bird.");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to dolphins
     * @param d
     */
    public void speak(Dolphin d)
    {
        System.out.println(this.name + " the bird says Chirp Chirp to " + d.getName() + " the dolphin.");
    }

    public double getFlightHeight()
    {
        return this.flightHeight;
    }

    public String getName()
    {
        return this.name;
    }

    public int getAge()
    {
        return this.age;
    }

    public void setFlightHeight(double newFlightHeight)
    {
        this.flightHeight = newFlightHeight;
    }

    public void setName(String newName)
    {
        this.name = newName;
    }

    public void setAge(int newAge)
    {
        this.age = newAge;
    }
}
