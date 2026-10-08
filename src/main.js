// Menzil · Gök — step 1: real imagery stage.
// Google Photorealistic 3D Tiles over the Gulf of Finland, viewed top-down like the game map.
import {
  Viewer, GoogleMaps, createGooglePhotorealistic3DTileset, Cartesian3, Cartesian2,
  Math as CMath, Color, LabelStyle, VerticalOrigin, HeightReference, PolylineDashMaterialProperty,
  Transforms, Matrix4, Ellipsoid, Cartographic, ScreenSpaceEventType, defined,
} from 'cesium';
import 'cesium/Build/Cesium/Widgets/widgets.css';
import './style.css';

const KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

// ---- game frame: a 360 × 240 km rectangle centred on the gulf, x east, y south (same as the game's world units)
export const FRAME = { lat: 59.80, lon: 24.85, wKm: 360, hKm: 240, unitM: 50 };
const center = Cartesian3.fromDegrees(FRAME.lon, FRAME.lat, 0);
const enu = Transforms.eastNorthUpToFixedFrame(center);
// world units (x right/east, y down/south, origin top-left) → Cartesian3 on the ellipsoid
export function worldToCartesian(x, y, h = 0) {
  const eM = x * FRAME.unitM - FRAME.wKm * 500, nM = FRAME.hKm * 500 - y * FRAME.unitM;
  const p = Matrix4.multiplyByPoint(enu, new Cartesian3(eM, nM, 0), new Cartesian3());
  const c = Ellipsoid.WGS84.cartesianToCartographic(p);
  return Cartesian3.fromRadians(c.longitude, c.latitude, h);
}

function fail(text) { const m = document.getElementById('msg'); m.hidden = false; m.textContent = text; }

async function main() {
  if (!KEY) { fail('Google Maps API anahtarı tanımlı değil. Vercel → Settings → Environment Variables → VITE_GOOGLE_MAPS_API_KEY'); return; }
  GoogleMaps.defaultApiKey = KEY;

  const viewer = new Viewer('globe', {
    baseLayer: false, baseLayerPicker: false, geocoder: false, homeButton: false, sceneModePicker: false,
    navigationHelpButton: false, animation: false, timeline: false, fullscreenButton: false, infoBox: false,
    selectionIndicator: false, requestRenderMode: false,
  });
  const scene = viewer.scene;
  window.__viewer = viewer;                       // debug handle
  scene.globe.show = false;                       // the photorealistic tiles carry their own terrain and imagery
  scene.skyAtmosphere.show = true;
  scene.screenSpaceCameraController.minimumZoomDistance = 30;
  scene.screenSpaceCameraController.maximumZoomDistance = 900000;

  try {
    const tiles = await createGooglePhotorealistic3DTileset({ onlyUsingWithGoogleGeocoder: true });
    scene.primitives.add(tiles);
    window.__tiles = tiles;
    tiles.tileFailed.addEventListener((e) => console.error("tile failed", e.url, e.message));
  } catch (e) {
    fail('Google 3D görüntüleri yüklenemedi: ' + (e && e.message ? e.message : e) + '\nAnahtarın Map Tiles API için açık ve bu alan adına izinli olduğundan emin ol.');
    return;
  }

  // frame outline and the two headquarters, just to see the game area on real ground
  const corners = [[0, 0], [7200, 0], [7200, 4800], [0, 4800], [0, 0]].map(([x, y]) => worldToCartesian(x, y));
  viewer.entities.add({ polyline: { positions: corners, width: 1.5, clampToGround: true,
    material: new PolylineDashMaterialProperty({ color: Color.fromCssColorString('#9fd2dc').withAlpha(0.7), dashLength: 18 }) } });
  const pin = (lon, lat, text, css) => viewer.entities.add({
    position: Cartesian3.fromDegrees(lon, lat),
    point: { pixelSize: 9, color: Color.fromCssColorString(css), outlineColor: Color.BLACK, outlineWidth: 1, heightReference: HeightReference.CLAMP_TO_GROUND, disableDepthTestDistance: Number.POSITIVE_INFINITY },
    label: { text, font: '600 13px "IBM Plex Sans Condensed", sans-serif', fillColor: Color.fromCssColorString(css), outlineColor: Color.BLACK, outlineWidth: 3,
      style: LabelStyle.FILL_AND_OUTLINE, verticalOrigin: VerticalOrigin.BOTTOM, pixelOffset: new Cartesian2(0, -12),
      heightReference: HeightReference.CLAMP_TO_GROUND, disableDepthTestDistance: Number.POSITIVE_INFINITY },
  });
  pin(24.94, 60.17, 'Kuzey · Komuta', '#9fd2dc');
  pin(24.75, 59.44, 'Güney · Komuta', '#ff7563');

  // start straight above the gulf, the way the game map opens
  viewer.camera.setView({
    destination: Cartesian3.fromDegrees(FRAME.lon, FRAME.lat, 420000),
    orientation: { heading: 0, pitch: CMath.toRadians(-90), roll: 0 },
  });

  // HUD: altitude and how many metres one screen pixel covers
  const hud = document.getElementById('hud');
  scene.postRender.addEventListener(() => {
    const h = viewer.camera.positionCartographic.height;
    const mpp = (2 * h * Math.tan(viewer.camera.frustum.fovy / 2)) / scene.canvas.clientHeight;
    hud.innerHTML = `<b>MENZİL · GÖK</b><div>İrtifa <span>${h > 2000 ? (h / 1000).toFixed(1) + ' km' : Math.round(h) + ' m'}</span></div><div>Piksel <span>${mpp > 1 ? mpp.toFixed(1) + ' m' : Math.round(mpp * 100) + ' cm'}</span></div><div>Fin Körfezi <span>59,8° K · 24,9° D</span></div>`;
  });
}
main();
