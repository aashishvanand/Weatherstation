package aashish.com.weatherstation;

import android.app.ProgressDialog;
import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.CardView;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;
import com.android.volley.Request;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    private ProgressDialog pDialog;
    TextView temperature_textview,pressure_textview,seapressure_textview,humidity_textview,
            latitude_textview,longitude_textview,altitude_textview,lightintensity_textview,co2_textview,rainfall_textview,
            lastupdated_textview;
    String temperature,pressure,seapressure,humidity,latitude,longitude,altitude,lightintensity,co2,rainfall,lastupdated;
    CardView compass;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Progress dialog
        pDialog = new ProgressDialog(this);
        pDialog.setCancelable(false);
        getdata();
        temperature_textview = (TextView) findViewById(R.id.temperature);
        pressure_textview = (TextView) findViewById(R.id.pressure);
        seapressure_textview = (TextView) findViewById(R.id.seapressure);
        humidity_textview = (TextView) findViewById(R.id.humidity);
        latitude_textview = (TextView) findViewById(R.id.latitude);
        longitude_textview = (TextView) findViewById(R.id.longitude);
        altitude_textview = (TextView) findViewById(R.id.altitude);
        lightintensity_textview = (TextView) findViewById(R.id.lightintensity);
        co2_textview = (TextView) findViewById(R.id.co2);
        rainfall_textview = (TextView) findViewById(R.id.rainfall);
        lastupdated_textview = (TextView) findViewById(R.id.lastupdated);
        compass = (CardView) findViewById(R.id.compass);

        compass.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                String coordinates = String.format("geo:0,0?q=" + latitude + "," + longitude);
                Intent intentMap = new Intent( Intent.ACTION_VIEW, Uri.parse(coordinates) );
                startActivity( intentMap );
            }
        });

    }

    private void getdata()
    {
        // Tag used to cancel the request
        String tag_string_req = "get_data";

        pDialog.setMessage("Downloading..");
        showDialog();

        StringRequest strReq = new StringRequest(Request.Method.GET,
                BuildConfig.URL, new com.android.volley.Response.Listener<String>() {

            @Override
            public void onResponse(String response) {
                hideDialog();

                try {
                    JSONObject jObj = new JSONObject(response);
                    boolean error = jObj.getBoolean("error");
                    // Check for error node in json
                    if (!error) {
                        // user successfully logged in
                        // Now store the user in SQLite
                        temperature = jObj.getString("temperature");
                        pressure = jObj.getString("pressure");
                        seapressure = jObj.getString("seapressure");
                        humidity = jObj.getString("humidity");
                        latitude = jObj.getString("latitude");
                        longitude = jObj.getString("longitude");
                        altitude = jObj.getString("altitude");
                        lightintensity = jObj.getString("lightintensity");
                        co2 = jObj.getString("co2");
                        rainfall = jObj.getString("rainfall");
                        lastupdated = jObj.getString("lastupdated");

                        temperature_textview.setText("Temperature " + temperature + " °C");
                        pressure_textview.setText("Atm " + pressure + " Pa");
                        seapressure_textview.setText("Sea " + seapressure + " Pa");
                        humidity_textview.setText("Humidity " + humidity + "%");
                        latitude_textview.setText("Latitude " + latitude);
                        longitude_textview.setText("Longitude " + longitude);
                        altitude_textview.setText("Altitude " + altitude + " m");
                        //lightintensity_textview.setText("Lightintensity :" + lightintensity +"lx");
                        //co2_textview.setText("Co2 :" + co2 + "ppm");
                        //rainfall_textview.setText("Rainfall :" + rainfall + "cm");
                        lightintensity_textview.setText("Coming Soon");
                        co2_textview.setText("Coming Soon");
                        rainfall_textview.setText("Coming Soon");
                        lastupdated_textview.setText("Updated " + lastupdated);


                    } else {
                        // Error in login. Get the error message
                        Toast.makeText(getApplicationContext(),
                                "Data not found!", Toast.LENGTH_LONG).show();
                    }
                } catch (JSONException e) {
                    // JSON error
                    e.printStackTrace();
                    Toast.makeText(getApplicationContext(), "Unknown Error", Toast.LENGTH_LONG).show();
                }

            }
        }, new com.android.volley.Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(getApplicationContext(),
                        error.getMessage(), Toast.LENGTH_LONG).show();
                hideDialog();
            }
        });
        AppController.getInstance().addToRequestQueue(strReq, tag_string_req);
    }

    private void showDialog() {
        if (!pDialog.isShowing())
            pDialog.show();
    }

    private void hideDialog() {
        if (pDialog.isShowing())
            pDialog.dismiss();
    }
}
