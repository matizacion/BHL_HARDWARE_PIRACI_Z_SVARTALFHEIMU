using System.Collections;
using System.Text;
using System.Net;

using System.Threading;
using System.Collections.Generic;
using UnityEngine;
using System.Net.Sockets;
using System;

using System.Net;
using System.Net.Sockets;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using UnityEngine.UI;


public class master : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject sphere_model;
    public GameObject[] spheres = new GameObject[21];
    public int port = 5052;
    public Text IP_target;
   

    bool startReciving = true;
    void Start()
    {
        IP_target = GameObject.Find("Text_IP").GetComponent<Text>();
        IP_target.text = IPManager.GetIP(ADDRESSFAM.IPv4);

        for (int i = 0; i < 21; i++)
        {
            spheres[i] = Instantiate(sphere_model, new Vector3(0, 0, 0), Quaternion.identity);
        }

        

    }

    public void set_color(int id , Color c)
    {
        var cubeRenderer = spheres[id].GetComponent<Renderer>();
        cubeRenderer.material.SetColor("_Color", c);
    }

    public void start_spheres()
    {
        for (int i = 0; i < 21; i++)
        {
            spheres[i] = Instantiate(sphere_model, new Vector3(0, 0, 0), Quaternion.identity);
        }
    }



    // Update is called once per frame
    void Update()
    {
       
    }
    public void receive_method()
    {
     
    }

    public static string LocalIPAddress()
    {
        IPHostEntry host;
        string localIP = "0.0.0.0";
        host = Dns.GetHostEntry(Dns.GetHostName());
        foreach (IPAddress ip in host.AddressList)
        {
            if (ip.AddressFamily == AddressFamily.InterNetwork)
            {
                localIP = ip.ToString();
                break;
            }
        }
        return localIP;
    }

    public class IPManager
    {
        public static string GetIP(ADDRESSFAM Addfam)
        {
            //Return null if ADDRESSFAM is Ipv6 but Os does not support it
            if (Addfam == ADDRESSFAM.IPv6 && !Socket.OSSupportsIPv6)
            {
                return null;
            }

            string output = "0.0.0.0";

            foreach (NetworkInterface item in NetworkInterface.GetAllNetworkInterfaces())
            {
#if UNITY_EDITOR_WIN || UNITY_STANDALONE_WIN
                NetworkInterfaceType _type1 = NetworkInterfaceType.Wireless80211;
                NetworkInterfaceType _type2 = NetworkInterfaceType.Ethernet;

                if ((item.NetworkInterfaceType == _type1 || item.NetworkInterfaceType == _type2) && item.OperationalStatus == OperationalStatus.Up)
#endif
                {
                    foreach (UnicastIPAddressInformation ip in item.GetIPProperties().UnicastAddresses)
                    {
                        //IPv4
                        if (Addfam == ADDRESSFAM.IPv4)
                        {
                            if (ip.Address.AddressFamily == AddressFamily.InterNetwork)
                            {
                                if (ip.Address.ToString() != "127.0.0.1")
                                    output = ip.Address.ToString();
                            }
                        }

                        //IPv6
                        else if (Addfam == ADDRESSFAM.IPv6)
                        {
                            if (ip.Address.AddressFamily == AddressFamily.InterNetworkV6)
                            {
                                if (ip.Address.ToString() != "127.0.0.1")
                                    output = ip.Address.ToString();
                            }
                        }
                    }
                }
            }
            return output;
        }
    }

    public enum ADDRESSFAM
    {
        IPv4, IPv6
    }

}
