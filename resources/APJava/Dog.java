package classesPt1;

public class Dog {

    // Class/static variables
    public static int dogsCreated = 0;

    // Properties (Fields)
    private String name;
    private String breed;
    private int age;
    
    // Constructor
    public Dog(String name, String dBreed, int dAge)
    {
        this.name = name;
        breed = dBreed;
        age = dAge;
        dogsCreated++;
    }

    // Overloaded Constructor, 1 parameter instead of 3
    public Dog(String name)
    {
        this.name = name;
        dogsCreated++;
    }

    public Dog()
    {
        this("Derek", "Jin", 2);
    }

    public void sayHello()
    {
        System.out.println("Ruff ruff my name is " + name);
    }

    public String getName()
    {
        return name;
    }

    public void setName(String newName)
    {
        this.name = newName;
    }

    public int getAge()
    {
        return this.age;
    }

    public void setAge(int age)
    {
        this.age = age;
    }

    public int getDogsCreated()
    {
        return dogsCreated;
    }
}
