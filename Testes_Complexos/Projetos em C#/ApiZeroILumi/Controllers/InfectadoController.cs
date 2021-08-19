using System;
using ApiZeroILumi.Data.Collections;
using ApiZeroILumi.Models;
using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;


namespace ApiZeroILumi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class InfectadoController : ControllerBase
    {
        Data.MongoDB _mongoDB;
        IMongoCollection<Infectado> _infectadosCollection;
        private DateTime _DatadeNascimento;

        public InfectadoController(Data.MongoDB mongoDB)
        {
            _mongoDB = mongoDB;
            _infectadosCollection = _mongoDB.DB.GetCollection<Infectado>(typeof(Infectado).Name.ToLower());
        }

        [HttpPost]
        public ActionResult SalvarInfectado([FromBody] InfectadoDto dto)
        {
            var infectado = new Infectado(dto.DataNascimento, dto.Sexo, dto.Latitude, dto.Longitude);

            _infectadosCollection.InsertOne(infectado);
            
            return StatusCode(201, "Infectado adicionado com sucesso");
        }

        [HttpGet]
        public ActionResult ObterInfectados()
        {
            var infectados = _infectadosCollection.Find(Builders<Infectado>.Filter.Empty).ToList();
            
            return Ok(infectados);
        }

        [HttpPut]
        public ActionResult AtualizarInfectado([FromBody] InfectadoDto dto)
        {

            _infectadosCollection.UpdateOne(Builders<Infectado>.Filter.Where(_ => _DatadeNascimento == dto.DataNascimento),Builders<Infectado>.Update.Set("sexo",dto.Sexo));
            
            return Ok("Atualizado com sucesso");
        }

        [HttpDelete("{dataNasc}")]
        public ActionResult Delete(string dataNasc)
        {
          
            _infectadosCollection.DeleteOne(Builders<Infectado>.Filter.Where(_ => _DatadeNascimento == Convert.ToDateTime(dataNasc)));
            
            return Ok("Deletado com sucesso");
        }


    }
}