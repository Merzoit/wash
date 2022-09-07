const data = [
  {
    value: 'Тестовая услуга',
    1: 200,
    B: 250,
    C: 300,
    D: 350
  },
  {
    value: 'Тест 2',
    1: 150,
    B: 200,
    C: 250,
    D: 250
  },
  {
    value: 'тест 3',
    1: 150,
    B: 200,
    C: 250,
    D: 250
  },
]

const services = document.querySelector('#id_service')
const selectedService = services.selectedOptions

const price = document.querySelector('#id_price')

const getCalculation = document.querySelector('.onValue')

const carClass = document.querySelector('#id_car_class')
const selectedCarClass = carClass.value

const premiumElement = document.querySelector('#premium')

getCalculation.addEventListener('click', setValue)

let serviceValues = []

function setValue() {
  for (let option of selectedService) {
    serviceValues.push(option.textContent)
  }
  calculation(serviceValues)
  serviceValues = []
}

function calculation(serviceValues) {
  const sum = []
  for (let value of serviceValues) {
    data.forEach(elem => {
      if (elem.value === value) {
        sum.push(elem[selectedCarClass])
      }
    })
  }
  const result = sum.reduce((previousValue, currentValue) => {
    return previousValue + currentValue
  }, 0)

  price.value = Number(result) + Number(premiumElement.value)
}


