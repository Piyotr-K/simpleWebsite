using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gun : MonoBehaviour
{
    public GameObject hitFx;

    public bool isAuto = false;

    public int clipSize = 30;
    public int currentClip = 0;

    public float reloadTime = 0.75f;
    private float reloadLeft = 0;

    public float fireTime = 0.5f;
    private float fireTimeLeft = 0;

    public bool doubleDamage = false;

    // Start is called before the first frame update
    void Start()
    {
        currentClip = clipSize;
    }

    // Update is called once per frame
    void Update()
    {
        fireTimeLeft -= Time.deltaTime;

        if (Input.GetKeyDown(KeyCode.Q))
            doubleDamage = true;

        if (Input.GetKeyDown(KeyCode.R))
            reload();

        if (reloadLeft > 0)
        {
            reloadLeft -= Time.deltaTime;
            if (reloadLeft <= 0)
            {
                currentClip = clipSize;
                Debug.Log("Ammo count after reloading: " + currentClip);
            }
            else
                return;
        }

        if (isAuto)
        {
            if (fireTimeLeft > 0)
                return; // Return to stop the method from going further
            // If the user clicks with their left click
            if (Input.GetMouseButton(0))
                fire();
        }
        else
        {
            if (Input.GetMouseButtonDown(0))
                fire();
        }
    }

    void fire()
    {
        RaycastHit hitInfo;

        fireTimeLeft = fireTime;

        if (currentClip > 0)
        {
            // Everytime we shoot we lose a bullet
            currentClip--;
            Debug.Log("Ammo count: " + currentClip);
            // Cast a ray from the center of the screen until it hits something, or not
            if (Physics.Raycast(Camera.main.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0)), out hitInfo))
            {
                // Spawn particle system
                GameObject go = Instantiate(hitFx);
                // Move particle system to where we shoot
                go.transform.position = hitInfo.point;
                // Point the particle system in the right direction
                go.transform.forward = hitInfo.normal;

                // Only hitting objects that are "shootable"
                Shootable hit = hitInfo.collider.GetComponent<Shootable>();
                if (hit != null)
                {
                    if (doubleDamage)
                        hit.OnHit(2);
                    else
                        hit.OnHit(1);
                }
            }
        }
        else
        {
            reload();
        }
    }

    void reload()
    {
        if (reloadLeft <= 0)
        {
            reloadLeft = reloadTime;
        }
    }
}
