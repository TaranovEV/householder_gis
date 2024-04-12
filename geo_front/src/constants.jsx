const opponentsColumns = [
  {
    id: 'name',
    label: 'Магазин',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'address',
    label: 'Адрес',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'distance',
    label: 'Расстояние, м',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toFixed(2),
  },
];

function createOppoData(shop, adress, distance) {
  return { shop, adress, distance };
}


const ourShopsColumns = [
  {
    id: 'address',
    label: 'Адрес',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'square',
    label: 'Площадь,\u00a0м\u00b2',
    minWidth: 50,
    maxWidth: 55,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'distance',
    label: 'Расстояние, м',
    minWidth: 50,
    align: 'center',
    format: (value) => value.toFixed(2),
  },
];

function createOurShopsData(shop, adress, square, distance) {
  return { shop, adress, square, distance };
}


const publicTransportColumns = [
  {
    id: 'name',
    label: 'Остановки',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'route_numbers',
    label: 'Маршруты',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
];

function createPublicTransport(stops, routes) {
  return { stops, routes };
}


const subwayColumns = [
  {
    id: 'name',
    label: 'Станция',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'incoming_passengers',
    label: 'Пассажиропоток, мес',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
];

function createSubway(station, traffic) {
  return { station, traffic };
}

const baseApiUrl = 'http://localhost:8090'
export {opponentsColumns , ourShopsColumns, publicTransportColumns, subwayColumns, baseApiUrl};
