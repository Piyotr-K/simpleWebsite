using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerHealth : Shootable
{
    // Player's max health
    public int maxHealth = 10;

    // Start is called before the first frame update
    void Start()
    {
        health = maxHealth;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.H)) OnHit(1);
    }

    public override void OnHit(int dmg)
    {
        health -= dmg;
        
        if (health < 0)
        {
            Destroy(GetComponent<PlayerMovement>());
            Rigidbody rb = GetComponent<Rigidbody>();
            rb.constraints = RigidbodyConstraints.None;
        }
    }
}
