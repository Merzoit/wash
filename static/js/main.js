const data = [
  {
    value: 'Тестовая услуга',
    A: 200,
    B: 250,
    C: 300,
    D: 350
  },
  {
    value: 'Тест 2',
    A: 150,
    B: 200,
    C: 250,
    D: 250
  },
  {
    value: 'тест 3',
    A: 150,
    B: 200,
    C: 250,
    D: 250
  },
]

const services = document.querySelector('#id_service')
const selectedService = services.selectedOptions

const getCalculation = document.querySelector('.onValue')

getCalculation.addEventListener('click', setValue)

let serviceValues = []


function setValue() {
  for (let option of selectedService) {
    serviceValues.push(option.textContent)
  }
  calculation(serviceValues)
}

const carClass = document.querySelector('#id_car_class')
const selectedCarClass = carClass.textContent

const sum = []

function calculation(serviceValues) {


  for (let value of serviceValues) {
    console.log(selectedCarClass)
    console.log(value.A === carClass)
    data.forEach(elem => {
      if (elem.value === value) {
        sum.push(elem.A)
      }
    })
  }
  console.log(sum)
}


// const id_services = document.querySelector('#service')
// const option = document.createElement('option', )
//
// function createOptionList() {
//   const servicesLength = 5
//   for (let i = 0; i < servicesLength; i++) {
//     id_services.append(option)
//   }
// }
//
// createOptionList()