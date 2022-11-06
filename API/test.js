testfunction = async function() {
    //post request to an api
    const response = await fetch('http://3.91.155.146:5000'
    , {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "brightness": "0.5",
                "red": "255",
                "green": "235",
                "blue": "0",
                "frequency": "2",
                "area":"1"
                })
        });
    const data = await response.json();
    console.log(data);
}