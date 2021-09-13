public class Animal {

    private String name;
    private int age;

    // Animal constructor
    public Animal(String name, int age)
    {
        this.name = name;
        this.age = age;
        // System.out.println("Animal Constructor Called");
    }

    // public Animal() {}

    public String getName()
    {
        return name;
    }

    public int getAge()
    {
        return age;
    }

    public void setAge(int age)
    {
        this.age = age;
    }   

    public void normalSpeak()
    {
        System.out.println("Idk how an animal is supposed to speak \"Normally\"");
    }

    public void magicSpeak()
    {
        System.out.println("Hello my name is " + name + ". I am " + age + " years old.");
    }
}