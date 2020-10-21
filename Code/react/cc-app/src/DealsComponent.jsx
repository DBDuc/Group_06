import React, { useState, useEffect } from 'react';

function DealsComponent() {
  const [deals, setDeals] = useState([]);

  // Similar to componentDidMount and componentDidUpdate:
  useEffect(() => {
    // Update the document title using the browser API
    //document.title = `You clicked ${count} times`;

    //const apiUrl = 'http://localhost:8090/client/testservice';
    //fetch(apiUrl)
    //  .then((response) => response.json())
    //  .then((data) => console.log(deals));
    const decoder = new TextDecoder('utf-8')
    const dealsUrl = 'http://localhost:8090/deals';
    //fetch(dealsUrl)
    //  .then(response => {
    //  response.body
    //  .getReader()
    //  .read()
    //  .then(({value, done}) => {
     //   setDeals([...deals, decoder.decode(value)]);
      //  console.log(deals.length);
      //})
    //})


  });

  return (
    <div style={{overflow: "visible"}}>
        {deals}
    </div>
  );
}

export default DealsComponent;