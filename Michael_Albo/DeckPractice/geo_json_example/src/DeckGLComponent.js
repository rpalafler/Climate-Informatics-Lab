import React, {useState} from 'react'
import { DeckGL } from 'deck.gl'
import {GeoJsonLayer} from '@deck.gl/layers';
import DATA from './data.json';
//DATA FROM VIDEO DESCRIPTION: https://www.youtube.com/watch?v=bPlKPvUu_XA
//CODE MODIFIED FROM DECK.GL DOCUMENTATION: https://deck.gl/docs/api-reference/layers/geojson-layer

export const DeckGLComponent = () => {
    const [viewState, setViewState] = useState({
        latitude: 37.7749,
        longitude: -122.4194,
        zoom: 12,
      });
      const layer = new GeoJsonLayer({
        id: 'geojson-layer',
        data: DATA,
        pickable: true,
        stroked: false,
        filled: true,
        extruded: true,
        pointType: 'circle',
        lineWidthScale: 20,
        lineWidthMinPixels: 2,
        getFillColor: [160, 160, 180, 200],
        getPointRadius: 100,
        getLineWidth: 1,
        getElevation: 30
      });
    

  return (
    <DeckGL viewState={viewState} layers = {[layer]}  getTooltip={({object}) => object && (object.properties.name || object.properties.station)} />
  )
}
export default DeckGLComponent;