using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        // Get the user's A and D input
        float horizontal = Input.GetAxis("Horizontal");

        // A vector for the direction to move the player in
        Vector3 movement = new Vector3(horizontal, 0, 0);

        rb.velocity = movement;
    }
}