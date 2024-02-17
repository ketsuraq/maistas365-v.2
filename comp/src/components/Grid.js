import GridElement from "./GridElement"

const urlList = [
  'https://eparduotuve.iki.lt/product/IKI/Arbatinukas-11l',
  'https://eparduotuve.iki.lt/product/IKI/Saldainiai-RAFFAELLO-150-g',
  'https://eparduotuve.iki.lt/product/IKI/Kempine-SCRUB-DADDY',
  'https://eparduotuve.iki.lt/product/IKI/Lietuviski-ilgavaisiai-agurkai-1-vnt',
  'https://eparduotuve.iki.lt/product/IKI/Baltasis-akytasis-sokoladas-ROSHEN-85-g',
  'https://eparduotuve.iki.lt/product/IKI/Pieninis-sokoladas-su-akytojo-baltojo-sokolado-idaru-MILKA-90-g'
]

const Grid = () => {
  return (
    <div className="grid-container">
      {urlList.map((url, index) => (
        <GridElement key={index} url={url} />
      ))}
    </div>
  );
};

export default Grid