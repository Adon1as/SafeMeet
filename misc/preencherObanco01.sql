SET SQL_SAFE_UPDATES = 0;
use safemeet;

delete from pessoa where true;
insert into pessoa values('101', 'Ze da Silva', '1970-10-10','rua da cidade','ufrn','zap: 84 9946');
insert into pessoa values('102', 'Dalva Maria', '1980-10-10','cep 0001','ufrn','email: dalva2000@mail.com');

delete from participante where true;
insert into participante values('transporte publico','2012-06-18 10:34:09','2012-06-18 11:34:09 ',101);

delete from reponsavel where true;
insert into reponsavel values('diretora','102');

delete from atestado where true;
insert into atestado values(1,0x010203040506,'J45','101');

delete from local where true;
insert into local values(1,'uma sala','janelas','rua qualquer','15x20');

delete from evento where true;
insert into evento values(1,'2021-06-18 10:34:09','2021-06-28 10:34:09','00:15:00',2,'revisao de prova',1);

delete from participa where true;
insert into participa values('101',1,'2021-06-19 10:34:09','sim');

delete from reponsavel_has_evento where true;
insert into reponsavel_has_evento values('102',1,1);

delete from solicita_mudanca where true;
insert into solicita_mudanca values('2021-06-18 10:34:09','pq sim',false,'101',1);



