'use client'

interface ProductProps {
  params: {
    id: string
  }
}

export default function Product(props: ProductProps) {
  const buyItem = () => {
    console.log('Added to the cart!')
  }

  return (
    <>
      <h1>Product: {props.params.id}</h1>

      <button className="rounded-lg p-2 ring ring-red-500" onClick={buyItem}>
        Add to cart
      </button>
    </>
  )
}
