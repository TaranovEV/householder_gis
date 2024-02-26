const opponentsColumns = [
  {
    id: 'shop',
    label: 'Магазин',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'adress',
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

const opponentsRows = [
  createOppoData('Вкуссвилл', 'ул. Маршала Катукова 11', 50),
  createOppoData('Пятёрочка', 'ул. Маршала Катукова 111', 1403),
  createOppoData('Пятёрочка', 'ул. Маршала Катукова 112', 1403),
];

const ourShopsColumns = [
  {
    id: 'shop',
    label: 'Магазин',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'adress',
    label: 'Адрес',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'square',
    label: 'Площадь,\u00a0м\u00b2',
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

function createOurShopsData(shop, adress, square, distance) {
  return { shop, adress, square, distance };
}

const ourShopsRows = [
  createOurShopsData('Наш', 'ул. Маршала Катукова 11',150, 50),
  createOurShopsData('Наш', 'ул. Маршала Катукова 111',500, 1403),
  createOurShopsData('Наш', 'ул. Маршала Катукова 112', 300, 1403),
];

const publicTransportColumns = [
  {
    id: 'stops',
    label: 'Остановки',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'routes',
    label: 'Маршруты',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
];

function createPublicTransport(stops, routes) {
  return { stops, routes };
}

const publicTransportRows = [
  createPublicTransport('Маршала Катукова', [1, 2, 3]),
  createPublicTransport('Маршала Катукова', [1, 2, 3]),
  createPublicTransport('Маршала Катукова', [1, 2, 3]),
];

const subwayColumns = [
  {
    id: 'station',
    label: 'Станция',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'traffic',
    label: 'Пассажиропоток, мес',
    minWidth: 100,
    align: 'center',
    format: (value) => value.toLocaleString('en-US'),
  },
];

function createSubway(station, traffic) {
  return { station, traffic };
}

const subwaytRows = [
  createSubway('Щукинская', [1, 2, 3]),
  createSubway('Щукинская', [1, 2, 3]),
  createSubway('Щукинская', [1, 2, 3]),
];

export {opponentsColumns , opponentsRows, ourShopsColumns, ourShopsRows, publicTransportColumns, publicTransportRows, subwayColumns, subwaytRows};