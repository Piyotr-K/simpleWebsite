using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    //
    private Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        string test = "Hello"; // String, any english "sentence"
        int num = 5; // Integer, cannot have decimals
        float num2 = 0.5f; // Float, can have decimals, but if you have a decimal need to put f
        double deciNum = 0.5; // double, decimals always, very big

        // 
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        //
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        //
        Vector3 move = new Vector3(horizontal, 0, vertical);
        
        //
        if (move.magnitude > 1)
        {
            move = move.normalized;
        }

        //
        move.y = rb.velocity.y;
        rb.velocity = move;
    }

    // Homework:
    // Basic:
    // Comment your code, that is put the // explanation above most of your code
    // Change the move speed so that it is 5 instead of 1
    //
    // Challenge:
    // Have a sprint button (shift)
    // When the user presses shift, they move faster
}
