import React, { useState } from 'react';
import DeckGL from '@deck.gl/react';
import {BitmapLayer} from '@deck.gl/layers';
import {TileLayer} from '@deck.gl/geo-layers';
//CODE MODIFIED FROM DECK.GL DOCUMENTATION: https://deck.gl/docs/api-reference/geo-layers/tile-layer

const DeckGLComponent = () => {
const [viewState, setViewState] = useState({
    latitude: 37.7749,
    longitude: -122.4194,
    zoom: 12,
    });

    const layer = new TileLayer({
        // https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_servers
        data: 'https://c.tile.openstreetmap.org/{z}/{x}/{y}.png',
    
        minZoom: 0,
        maxZoom: 19,
        tileSize: 256,
    
        renderSubLayers: props => {
          const {
            bbox: {west, south, east, north}
          } = props.tile;
    
          return new BitmapLayer(props, {
            data: null,
            image: props.data,
            bounds: [west, south, east, north]
          });
        }
      });
  return (
    <DeckGL viewState={viewState} layers = {[layer]}/>
  )
}

export default DeckGLComponent;