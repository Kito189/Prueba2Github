import { useEffect, useState } from "react";

function Envios() {
  const [envios, setEnvios] = useState([]);
  const [facturaId, setFacturaId] = useState("");
  const [comentario, setComentario] = useState("");

  const cargarEnvios = async () => {
    const res = await fetch("http://localhost:5000/envios");
    const data = await res.json();
    setEnvios(data);
  };

  useEffect(() => {
    cargarEnvios();
  }, []);

  const registrarEnvio = async () => {
    if (!facturaId) {
      alert("Ingrese ID de factura");
      return;
    }

    await fetch("http://localhost:5000/envios", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        factura_id: Number(facturaId),
        comentario,
      }),
    });

    setFacturaId("");
    setComentario("");
    cargarEnvios();
  };

  return (
    <div>
      <h2 className="h4 mb-3">Despacho de Productos</h2>

      <div className="row g-3 mb-3">
        <div className="col-md-3">
          <input
            className="form-control"
            placeholder="ID Factura"
            value={facturaId}
            onChange={e => setFacturaId(e.target.value)}
          />
        </div>
        <div className="col-md-7">
          <input
            className="form-control"
            placeholder="Comentario"
            value={comentario}
            onChange={e => setComentario(e.target.value)}
          />
        </div>
        <div className="col-md-2 d-grid">
          <button className="btn btn-success" onClick={registrarEnvio}>
            Despachar
          </button>
        </div>
      </div>

      <div className="table-responsive">
        <table className="table table-striped table-hover align-middle">
          <thead className="table-light">
            <tr>
              <th>ID</th>
              <th>Factura</th>
              <th>Comentario</th>
            </tr>
          </thead>
          <tbody>
            {envios.map(e => (
              <tr key={e.id}>
                <td>{e.id}</td>
                <td>{e.factura_id}</td>
                <td>{e.comentario}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Envios;
