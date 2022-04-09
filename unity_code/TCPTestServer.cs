using System;
using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;

using UnityEngine.UI;

public class TCPTestServer : MonoBehaviour
{

	public Slider slider_1;
	public Slider slider_2;
	public Slider slider_3;
	public Slider slider_4;
	public Slider slider_5;
	public Slider slider_6;

	public Text text_1;
	public Text text_2;
	public Text text_3;
	public Text text_4;
	public Text text_5;

	public InputField input_1;
	public InputField input_2;
	public InputField input_3;
	public InputField input_4;
	public InputField input_5;

	public Toggle toogle_1;

	public bool is_editable = false;



	#region private members 	
	/// <summary> 	
	/// TCPListener to listen for incomming TCP connection 	
	/// requests. 	
	/// </summary> 	
	private TcpListener tcpListener;
	/// <summary> 
	/// Background thread for TcpServer workload. 	
	/// </summary> 	
	private Thread tcpListenerThread;
	/// <summary> 	
	/// Create handle to connected tcp client. 	
	/// </summary> 	
	private TcpClient connectedTcpClient;
	#endregion

	public GameObject hand_prefab;
	master hand_object;
	public string[] splitArray;
	bool isTHere = false;

	// Use this for initialization
	void Start()
	{
		
		slider_1 = GameObject.Find("Slider").GetComponent<Slider>();
		slider_2 = GameObject.Find("Slider (1)").GetComponent<Slider>();
		slider_3 = GameObject.Find("Slider (2)").GetComponent<Slider>();
		slider_4 = GameObject.Find("Slider (3)").GetComponent<Slider>();
		slider_5 = GameObject.Find("Slider (4)").GetComponent<Slider>();

		text_1 = GameObject.Find("Text").GetComponent<Text>();
		text_2 = GameObject.Find("Text (1)").GetComponent<Text>();
		text_3 = GameObject.Find("Text (2)").GetComponent<Text>();
		text_4 = GameObject.Find("Text (3)").GetComponent<Text>();
		text_5 = GameObject.Find("Text (4)").GetComponent<Text>();

		input_1 = GameObject.Find("InputField").GetComponent<InputField>();
		input_2 = GameObject.Find("InputField (1)").GetComponent<InputField>();
		input_3 = GameObject.Find("InputField (2)").GetComponent<InputField>();
		input_4 = GameObject.Find("InputField (3)").GetComponent<InputField>();
		input_5 = GameObject.Find("InputField (4)").GetComponent<InputField>();

		toogle_1 = GameObject.Find("Toggle").GetComponent<Toggle>();






		toogle_change();

		// Start TcpServer background thread 		
		tcpListenerThread = new Thread(new ThreadStart(ListenForIncommingRequests));
		tcpListenerThread.IsBackground = true;
		tcpListenerThread.Start();
		//hand_object = Instantiate(hand_prefab, new Vector3(0, 0, 0), Quaternion.identity).GetComponent<master>();
		//hand_object.start_spheres();
	}

	void set_1_val(int input)
    {
		text_1.text = input.ToString();
		slider_1.value = input;
	}

	void set_2_val(int input)
	{
		text_2.text = input.ToString();
		slider_2.value = input;
	}

	void set_3_val(int input)
	{
		text_3.text = input.ToString();
		slider_3.value = input;
	}

	void set_4_val(int input)
	{
		text_4.text = input.ToString();
		slider_4.value =  input;
	}

	void set_5_val(int input)
	{
		text_5.text = input.ToString();
		slider_5.value =  input;
	}

	public void send_button()
    {
		String send_mess = "S,";
		send_mess += Math.Round(slider_1.value).ToString() + ",";
		send_mess += Math.Round(slider_2.value).ToString() + ",";
		send_mess += Math.Round(slider_3.value).ToString() + ",";
		send_mess += Math.Round(slider_4.value).ToString() + ",";
		send_mess += Math.Round(slider_5.value).ToString();
		Debug.Log("send - " + send_mess);
		SendMessage(send_mess);

	}

	public void add_button()
    {
		String send_mess = "H,";
		send_mess += input_1.text + ",";
		send_mess += input_2.text + ",";
		send_mess += input_3.text + ",";
		send_mess += input_4.text + ",";
		send_mess += input_5.text ;

		input_1.text = "";
		input_2.text = "";
		input_3.text = "";
		input_4.text = "";
		input_5.text = "";

		Debug.Log("add - " + send_mess);
		SendMessage(send_mess);
	}

	public void toogle_change()
    {
	
		
	
		is_editable = toogle_1.isOn;
        if (is_editable)
        {
			slider_1.interactable = true;
			slider_2.interactable = true;
			slider_3.interactable = true;
			slider_4.interactable = true;
			slider_5.interactable = true;


        }
        else
        {
			slider_1.interactable = false;
			slider_2.interactable = false;
			slider_3.interactable = false;
			slider_4.interactable = false;
			slider_5.interactable = false;
		}

	}

	// Update is called once per frame
	void Update()
	{
		toogle_change();
		text_1.text = slider_1.value.ToString();
		text_2.text = slider_2.value.ToString();
		text_3.text = slider_3.value.ToString();
		text_4.text = slider_4.value.ToString();
		if (isTHere)
		{
			if (!is_editable) 
			{ 
				set_1_val(int.Parse(splitArray[0]));
				set_2_val(int.Parse(splitArray[1]));
				set_3_val(int.Parse(splitArray[2]));
				set_4_val(int.Parse(splitArray[3]));
				set_5_val(int.Parse(splitArray[4]));
			}
		}
		SendMessage(" ");
	}

	/// <summary> 	
	/// Runs in background TcpServerThread; Handles incomming TcpClient requests 	
	/// </summary> 	
	private void ListenForIncommingRequests()
	{
		try
		{
			// Create listener on localhost port 8052. 			
			tcpListener = new TcpListener(IPAddress.Parse(IPManager.GetIP(ADDRESSFAM.IPv4)), 5052);
			tcpListener.Start();
			Debug.Log("Server is listening");
			Byte[] bytes = new Byte[1024];
			while (true)
			{
				using (connectedTcpClient = tcpListener.AcceptTcpClient())
				{
					// Get a stream object for reading 					
					using (NetworkStream stream = connectedTcpClient.GetStream())
					{
						int length;
						// Read incomming stream into byte arrary. 						
						while ((length = stream.Read(bytes, 0, bytes.Length)) != 0)
						{
							var incommingData = new byte[length];
							Array.Copy(bytes, 0, incommingData, 0, length);
							// Convert byte array to string message. 							
							string clientMessage = Encoding.ASCII.GetString(incommingData);
							Debug.Log("client message received as: " + clientMessage);
							clientMessage = clientMessage.Replace("[", "");
							clientMessage = clientMessage.Replace("]", "");
							splitArray = clientMessage.Split(char.Parse(","));
							//int number = int.Parse(splitArray[0]);
							int numberttt;
							if (int.TryParse(splitArray[0], out numberttt))
							{
								isTHere = true;
							}
							
						}
					}
				}
			}
		}
		catch (SocketException socketException)
		{
			Debug.Log("SocketException " + socketException.ToString());
		}
	}
	/// <summary> 	
	/// Send message to client using socket connection. 	
	/// </summary> 	
	private void SendMessage(String message_rasp)
	{
		if (connectedTcpClient == null)
		{
			return;
		}

		try
		{
			// Get a stream object for writing. 			
			NetworkStream stream = connectedTcpClient.GetStream();
			if (stream.CanWrite)
			{
				string serverMessage = message_rasp;
				// Convert string message to byte array.                 
				byte[] serverMessageAsByteArray = Encoding.ASCII.GetBytes(serverMessage);
				// Write byte array to socketConnection stream.               
				stream.Write(serverMessageAsByteArray, 0, serverMessageAsByteArray.Length);

				Debug.Log("Server sent his message - should be received by client");
			}
		}
		catch (SocketException socketException)
		{
			Debug.Log("Socket exception: " + socketException);
		}
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