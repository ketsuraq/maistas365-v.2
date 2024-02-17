import React, { useEffect, useState } from 'react';

const GridElement = ({ url }) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
        try {
          const response = await fetch('http://localhost:5000/scrape', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
          });
          const jsonData = await response.json();
          setData(jsonData);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

    fetchData();
  }, [url]);

  return (
    <div className="grid-element">
      {data ? (
        <>
          <h2 className='grid-element-title'>{data.title}</h2>
          <p className='grid-element-price'>{data.price}</p>
          <p className='grid-element-discount'>{data.discount}</p>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default GridElement;
