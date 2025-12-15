import { useEffect, useState } from "react";

function Ordenes() {
  const [ordenes, setOrdenes] = useState([]);
  const [cliente, setCliente] = useState("");
  const [producto, setProducto] = useState("");
  const [precio, setPrecio] = useState("");

  const cargarOrdenes = async () => {
    const res = await fetch("http://localhost:5000/ordenes");
    const data = await res.json();
    setOrdenes(data);
  };

  useEffect(() => {
    cargarOrdenes();
  }, []);

  const crearOrden = async () => {
    await fetch("http://localhost:5000/ordenes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ cliente, producto, precio })
    });
    setCliente("");
    setProducto("");
    setPrecio("");
    cargarOrdenes();
  };

  return (
    <div>
      <h2 className="h4 mb-3">Órdenes de Compra</h2>

      <div className="row g-3 mb-3">
        <div className="col-md-4">
          <input
            className="form-control"
            placeholder="Cliente"
            value={cliente}
            onChange={e => setCliente(e.target.value)}
          />
        </div>
        <div className="col-md-4">
          <input
            className="form-control"
            placeholder="Producto"
            value={producto}
            onChange={e => setProducto(e.target.value)}
          />
        </div>
        <div className="col-md-3">
          <input
            className="form-control"
            placeholder="Precio"
            value={precio}
            onChange={e => setPrecio(e.target.value)}
          />
        </div>
        <div className="col-md-1 d-grid">
          <button className="btn btn-success" onClick={crearOrden}>
            Crear
          </button>
        </div>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover align-middle">
          <thead className="table-light">
            <tr>
              <th>ID</th>
              <th>Cliente</th>
              <th>Producto</th>
              <th>Precio</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {ordenes.map(o => (
              <tr key={o.id}>
                <td>{o.id}</td>
                <td>{o.cliente}</td>
                <td>{o.producto}</td>
                <td>${o.precio}</td>
                <td>{o.estado}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Ordenes;
