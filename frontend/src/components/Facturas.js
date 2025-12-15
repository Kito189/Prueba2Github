import { useEffect, useState } from "react";

function Facturas() {
  const [facturas, setFacturas] = useState([]);
  const [ordenId, setOrdenId] = useState("");

  const cargarFacturas = async () => {
    const res = await fetch("http://localhost:5000/facturas");
    const data = await res.json();
    setFacturas(data);
  };

  useEffect(() => {
    cargarFacturas();
  }, []);

  const emitirFactura = async () => {
    if (!ordenId) {
      alert("Ingrese ID de la orden");
      return;
    }

    await fetch("http://localhost:5000/facturas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ orden_id: Number(ordenId) }),
    });

    setOrdenId("");
    cargarFacturas();
  };

  return (
    <div>
      <h2 className="h4 mb-3">Facturación</h2>

      <div className="row g-3 mb-3">
        <div className="col-md-4">
          <input
            className="form-control"
            placeholder="ID Orden"
            value={ordenId}
            onChange={e => setOrdenId(e.target.value)}
          />
        </div>
        <div className="col-md-2 d-grid">
          <button className="btn btn-success" onClick={emitirFactura}>
            Emitir
          </button>
        </div>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover align-middle">
          <thead className="table-light">
            <tr>
              <th>ID</th>
              <th>Orden</th>
              <th>IVA</th>
              <th>Total</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {facturas.map(f => (
              <tr key={f.id}>
                <td>{f.id}</td>
                <td>{f.orden_id}</td>
                <td>{f.iva}</td>
                <td>{f.total}</td>
                <td>{f.estado}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Facturas;
