const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const birthYear = Number(document.querySelector('#birthYear').value);
  const tariff = document.querySelector('#tariff').value;

  const currentYear = new Date().getFullYear();
  const age = currentYear - birthYear;

  let cost;

  if (age >= 50 || age < 14) {
    cost = 0;
  } else if (age >= 14 && age <= 24) {
    cost = calculateCost(tariff) / 2;
  } else {
    cost = calculateCost(tariff);
  }

  const result = document.querySelector('#result');
  result.innerHTML = `Стоимость проездного: ${cost} рублей`;
});

function calculateCost(tariff) {
  switch (tariff) {
    case 'hour':
      return 60;
    case 'week':
      return 300;
    case 'month':
      return 1000;
    case 'year':
      return 10000;
  }
}


