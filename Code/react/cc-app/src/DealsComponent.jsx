import React, { useState, useEffect } from 'react';

function DealsComponent() {
  const [deals, setDeals] = useState([]);

  // Similar to componentDidMount and componentDidUpdate:
  useEffect(() => {
    const dealsUrl = 'http://localhost:8090/json_example';

    fetch(dealsUrl)
    .then((response) => response.json())
    .then((data) => {
      let arr = [];
      data['deals'].forEach(element => {

        arr.push([element['data']['instrumentName'],element['data']['cpty'],element['data']['price'], element['data']['type'],element['data']['quantity'],element['data']['time'],])
      });
      setDeals(arr);
      console.log(data);
    });

  },[deals]);

  return (
    <div style={{overflow: "visible"}}>
        {deals}
    </div>
  );
}

export default DealsComponent;