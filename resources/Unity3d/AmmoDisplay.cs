using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class AmmoDisplay : MonoBehaviour
{
    private Text label;
    private Gun playerGun;

    // Start is called before the first frame update
    void Start()
    {
        label = GetComponent<Text>();
        // Gets the gun that the player is using
        // Gun being the gun script that we wrote
        playerGun = FindObjectOfType<PlayerMovement>().GetComponentInChildren<Gun>();
    }

    // Update is called once per frame
    void Update()
    {
        label.text = "Ammo Left: " + playerGun.currentClip.ToString();
    }
}