using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    // The player controller
    private Rigidbody rb;

    //
    private Camera cam;

    // Movement Variables
    public int walkSpeed = 5;
    public int runSpeed = 10;

    //
    public int lookXSensitivity = 2;
    public int lookYSensitivity = 2;

    // 
    public float maxXRotation = 60;
    private float currentRotation;

    // Start is called before the first frame update
    void Start()
    {
        string test = "Hello"; // String, any english "sentence"
        int num = 5; // Integer, cannot have decimals
        float num2 = 0.5f; // Float, can have decimals, but if you have a decimal need to put f
        double deciNum = 0.5; // double, decimals always, very big

        // At the start get the component
        rb = GetComponent<Rigidbody>();

        // 
        cam = GetComponentInChildren<Camera>();
    }

    // Update is called once per frame
    void Update()
    {
        // 
        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");

        // 
        transform.Rotate(0, mouseX * lookXSensitivity, 0);
        currentRotation -= mouseY * lookYSensitivity;

        // 
        currentRotation = Mathf.Clamp(currentRotation, -maxXRotation, maxXRotation);
        cam.transform.localEulerAngles = new Vector3(currentRotation, 0, 0);

        // Get the inputs for x and z axes
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        // Create a new movement force
        Vector3 move = new Vector3(horizontal, 0, vertical);
        
        // Set magnitude to 1 and remove decimals
        if (move.magnitude > 1)
        {
            move = move.normalized;
        }

        //
        move = transform.TransformVector(move);

        // If the user holds left shift, we sprint
        if (Input.GetKey(KeyCode.LeftShift))
        {
            move *= runSpeed;
        }
        else
        {
            move *= walkSpeed;
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (rb.position.y < 1.1)
            {
                rb.AddForce(0, 300, 0);
            }
        }

        // Prevent the player from floating
        move.y = rb.velocity.y;

        // Move the player
        rb.velocity = move;
    }

    // Function
    // Choice of putting something in (or not)
    // Choice of getting something out (or not)
    public bool test(int num)
    {
        Debug.Log("Test method");

        if (num > 5)
            return true;
        else
            return false;
    }
}
