import React, { useState, useEffect } from 'react';

function DealsComponent() {
  const [deals, setDeals] = useState('');

  // Similar to componentDidMount and componentDidUpdate:
  useEffect(() => {
    // Update the document title using the browser API
    //document.title = `You clicked ${count} times`;

    const apiUrl = 'http://localhost:8090/client/testservice';
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => setDeals(data['price']));
  });

  return (
    <div>
        {deals}
    </div>
  );
}

export default DealsComponent;