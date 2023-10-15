-- use pnad_covid

-- Copiando estrutura para tabela pnad_covid.a003

-- DROP TABLE IF EXISTS depara_respostas;
/*CREATE TABLE IF NOT EXISTS depara_respostas (
  `id` int NOT NULL AUTO_INCREMENT,
  respostas_id int,
  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Copiando dados para a tabela pnad_covid.depara_respostas
REPLACE INTO depara_respostas (`id`, respostas_id, `name`) VALUES
	(1, 1, 'Sim'),
	(2, 2, 'Não '),
	(3, 3, 'Não sabe'),
	(4, 9, 'Ignorado');

select * from depara_respostas ;*/

create or replace view pnad_covid_view AS
select 
	 convert(concat(dc.ano,'-',dc.`V1013`,'-01'), DATE) as 'data',
	 uf.name 											as uf,
	 cap.name 											as capital,
	 situ_domi.name 									as situacao_domicilio,
	 ifnull(reg_metro.name,	  "Não Aplicável")			as regiao_metropolitana, #Poucas linhas preenchidas, necessário verificar nos outros arquivos
	 tp_area.name 										as tipo_area,
	 cond_domi.name 									as condicao_domicilio,
	 dc.A002 											as idade,
	 sexo.name 										    as sexo,
	 raca.name  										as cor_raca,
	 esco.name 											as escolaridade,
	 ifnull(depara1.name,  	  "Não Aplicável")			as questao_febre,
	 ifnull(depara2.name,  	  "Não Aplicável")			as questao_tosse,
	 ifnull(depara3.name,  	  "Não Aplicável")			as questao_garganta,
	 ifnull(depara4.name,  	  "Não Aplicável")			as questao_dif_respirar,
	 ifnull(depara5.name,  	  "Não Aplicável")			as questao_dor_cabeca,
	 ifnull(depara6.name,  	  "Não Aplicável")			as questao_dor_peito,
	 ifnull(depara7.name,  	  "Não Aplicável")			as questao_nausea,
	 ifnull(depara8.name,  	  "Não Aplicável")			as questao_coriza,
	 ifnull(depara9.name,  	  "Não Aplicável")			as questao_fadiga,
	 ifnull(depara10.name, 	  "Não Aplicável")			as questao_dor_olhos,
	 ifnull(depara11.name, 	  "Não Aplicável")			as questao_cheiro_sabor,
	 ifnull(depara12.name, 	  "Não Aplicável")			as questao_dor_muscular,
	 ifnull(depara13.name, 	  "Não Aplicável")			as questao_estabelecimento_saude,
	 ifnull(depara14.name, 	  "Não Aplicável")			as questao_permaneceu_casa,
	 ifnull(depara15.name, 	  "Não Aplicável")			as questao_contato_saude,
	 ifnull(depara16.name,    "Não Aplicável")			as questao_remedio_conta_propria,
	 ifnull(depara17.name, 	  "Não Aplicável")			as questao_remedio_orientacao_medica,
	 ifnull(depara18.name, 	  "Não Aplicável")			as questao_visita_sus,
	 ifnull(depara19.name,    "Não Aplicável")			as questao_visita_participar,
	 ifnull(depara20.name, 	  "Não Aplicável")			as questao_outras_providencias,
	 ifnull(depara21.name, 	  "Não Aplicável")			as questao_buscou_atendimento,
	 ifnull(depara22.name, 	  "Não Aplicável")			as questao_buscou_PS_SUS_UPA,
	 ifnull(depara23.name, 	  "Não Aplicável")			as questao_hospital_SUS,
	 ifnull(depara24.name, 	  "Não Aplicável")			as questao_atendimento_privado,
	 ifnull(depara25.name, 	  "Não Aplicável")			as questao_ps_privado,
	 ifnull(depara26.name, 	  "Não Aplicável")			as questao_hospital_privado,
	 ifnull(internado.name,	  "Não Aplicável")	     	as questao_internado_mais_dias,
	 ifnull(depara27.name, 	  "Não Aplicável")			as questao_internacao_ajuda_respirar,
	 ifnull(depara28.name, 	  "Não Aplicável")			as questao_plano_saude,
	 ifnull(depara29.name,    "Não Aplicável")			as questao_trabalhou_semana_passada,
	 ifnull(depara30.name, 	  "Não Aplicável")			as questao_afastado_semana_passada,
	 ifnull(motivo_afast.name,"Não Aplicável")			as questao_motivo_afastamento,
	 ifnull(remunerado.name,  "Não Aplicável")			as questao_trabalha_remunerado,
	 ifnull(afastado.name,    "Não Aplicável")			as questao_tempo_afastado_trab,
	 dc.C0051											as afastado_1mes_1ano,
	 dc.C0052											as afastado_1ano_2anos,
	 dc.C0053											as afastado_02anos_98anos,
	 ifnull(depara31.name,	  "Não Aplicável")			as questao_mais_de_um_trabalho,
	 ifnull(descr_trab.name,  "Não Aplicável")    		as questao_descricao_trabalho,
	 ifnull(area_trab.name,	  "Não Aplicável")			as questao_area_trabalho,	 
	 ifnull(tipo_trab.name,	  "Não Aplicável")			as questao_carteira_assinada_outros,
	 ifnull(descr_tipo_trab.name, "Não Aplicável")   	as questao_tipo_trabalho_realizado,
	 ifnull(atividade_empr.name,  "Não Aplicável")		as atividade_da_empresa,
	 
	 case
	 	when C010 = 1 then rendimento.name
	 	else 'Não aplicável'
	 end 												as faixa_rendimento,
	 
	 case
	 	when C01012 = 2 then rendimento_prod.name
	 	else 'Não aplicável'
	 end												as faixa_rendimento_retirada_produtos,
	 
	 ifnull(beneficio.name,"Não Aplicável")				as recebia_beneficios,
	 
	 case
	 	when C011A = 1 then remuneracao_trab.name
	 	else 'Não aplicável'
	 end 												as remuneracao_produtos_mercadoria,
	 ifnull(trab_mesmo_local.name,"Não Aplicável")  	as questao_local_trabalho,		
	 ifnull(trab_remoto.name,	  "Não Aplicável")		as questao_trabalho_remoto,
	 ifnull(inss.name,	          "Não Aplicável")		as questao_contribuiu_inss,
	 ifnull(procurou_trab.name,	  "Não Aplicável")		as questao_procutou_trabalho,
	 ifnull(moti_n_trab.name,	  "Não Aplicável")		as questao_moti_nao_procurar_trabalho,
	 ifnull(depara32.name,		  "Não Aplicável")		as questao_gostaria_procurar_trabalho,
	 
	 case
	 	when dc.D0011 = 1 and dc.D0013 is not null then dc.D0013
	 	when dc.D0011 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as rendimento_aposentadoria_pensao,
	 
 	 case
	 	when dc.D0021 = 1 and dc.D0023 is not null then dc.D0023
	 	when dc.D0021 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as rendimento_pensao,
	 
 	 case
	 	when dc.D0031 = 1 and dc.D0033 is not null then dc.D0033
	 	when dc.D0031 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as rendimento_bolsa_familia,

 	 case
	 	when dc.D0041 = 1 and dc.D0043 is not null then dc.D0043
	 	when dc.D0041 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as rendimento_beneficios,
	 
 	 case
	 	when dc.D0051 = 1 and dc.D0053 is not null then dc.D0053
	 	when dc.D0051 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as auxlio_emergencia_covid,
	 
 	 case
	 	when dc.D0061 = 1 and dc.D0063 is not null then dc.D0063
	 	when dc.D0061 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as seguro_desemprego,
	
 	 case
	 	when dc.D0071 = 1 and dc.D0073 is not null then dc.D0073
	 	when dc.D0071 = 2 then 'Não'
	 	else 'Não aplicável'
	 end 												as redimentos_diversos,
	 domicilio.name  									as tipo_domicilio,
	 dc.F0021											as valor_pago_domicilio
from dados_covid dc
	left join uf 							on (dc.uf 		= uf.id)
	left join capital cap					on (dc.CAPITAL 	= cap.capital_id) 
	left join v1022 situ_domi 				on (dc.V1022 	= situ_domi.V1022_id)
	left join rm_ride reg_metro 			on (dc.RM_RIDE 	= reg_metro.RM_RIDE_id)
	left join v1023 tp_area 				on (dc.V1023 	= tp_area.V1023_id)
	left join a001a cond_domi 				on (dc.A001A 	= cond_domi.A001A_id)
	left join a003 sexo 					on (dc.A003 	= sexo.A003_id)
	left join a004 raca 					on (dc.A004 	= raca.A004_id)
	left join a005 esco 					on (dc.A005 	= esco.A005_id)
	left join depara_respostas depara1		on (dc.B0011 	= depara1.respostas_id)
	left join depara_respostas depara2		on (dc.B0012 	= depara2.respostas_id)
	left join depara_respostas depara3		on (dc.B0013	= depara3.respostas_id)
	left join depara_respostas depara4		on (dc.B0014 	= depara4.respostas_id)
	left join depara_respostas depara5		on (dc.B0015 	= depara5.respostas_id)
	left join depara_respostas depara6		on (dc.B0016 	= depara6.respostas_id)
	left join depara_respostas depara7		on (dc.B0017 	= depara7.respostas_id)
	left join depara_respostas depara8		on (dc.B0018 	= depara8.respostas_id)
	left join depara_respostas depara9		on (dc.B0019 	= depara9.respostas_id)
	left join depara_respostas depara10		on (dc.B00110	= depara10.respostas_id)
	left join depara_respostas depara11		on (dc.B00111 	= depara11.respostas_id)
	left join depara_respostas depara12		on (dc.B00112 	= depara12.respostas_id)
	left join depara_respostas depara13		on (dc.B002 	= depara13.respostas_id)
	left join depara_respostas depara14		on (dc.B0031 	= depara14.respostas_id)
	left join depara_respostas depara15		on (dc.B0032 	= depara15.respostas_id)
	left join depara_respostas depara16		on (dc.B0033 	= depara16.respostas_id)
	left join depara_respostas depara17		on (dc.B0034 	= depara17.respostas_id)
	left join depara_respostas depara18		on (dc.B0035 	= depara18.respostas_id)
	left join depara_respostas depara19		on (dc.B0036 	= depara19.respostas_id)
	left join depara_respostas depara20		on (dc.B0037 	= depara20.respostas_id)
	left join depara_respostas depara21 	on (dc.B0041 	= depara21.respostas_id)
	left join depara_respostas depara22		on (dc.B0042 	= depara22.respostas_id)
	left join depara_respostas depara23 	on (dc.B0043 	= depara23.respostas_id)
	left join depara_respostas depara24		on (dc.B0044 	= depara24.respostas_id)
	left join depara_respostas depara25		on (dc.B0045 	= depara25.respostas_id)
	left join depara_respostas depara26		on (dc.B0046 	= depara26.respostas_id)
	left join b005 internado				on (dc.b005		= internado.B005_id)
	left join depara_respostas depara27		on (dc.B006 	= depara27.respostas_id)
	left join depara_respostas depara28		on (dc.B007 	= depara28.respostas_id)
	left join depara_respostas depara29  	on (dc.C001		= depara29.respostas_id)
	left join depara_respostas depara30  	on (dc.C002		= depara30.respostas_id)
	left join c003 motivo_afast 			on (dc.C003		= motivo_afast.C003_id)
	left join c004 remunerado 				on (dc.C004 	= remunerado.C004_id)
	left join c005 afastado 				on (dc.C005 	= afastado.C005_id)
	left join depara_respostas depara31		on (dc.C006    	= depara31.respostas_id) 	 
	left join c007 descr_trab 				on (dc.C007 	= descr_trab.C007_id)
	left join c007a area_trab 				on (dc.C007A    = area_trab.C007A_id)
	left join c007b tipo_trab 		    	on (dc.c007B    = tipo_trab.C007B_id)
	left join c007c descr_tipo_trab         on (dc.c007C    = descr_tipo_trab.C007C_id)
	left join c007d atividade_empr			on (dc.c007d    = atividade_empr.C007D_id)
	left join C01011 rendimento 			on (dc.C01011   = rendimento.C01011_id)
	left join C0102 rendimento_prod 		on (dc.C0102    = rendimento_prod.C0102_id)
	left join C0103 beneficio 				on (dc.C0103    = beneficio.C0103_id)
	left join C011A11 remuneracao_trab 		on (dc.C011A11  = remuneracao_trab.C011A11_id)
	left join C012 trab_mesmo_local 		on (dc.C012 	= trab_mesmo_local.C012_id)
	left join C013 trab_remoto 				on (dc.C013     = trab_remoto.C013_id)
	left join C014 inss 					on (dc.C014     = inss.C014_id)
	left join C015 procurou_trab  			on (dc.c015     = procurou_trab.C015_id) 
	left join C016 moti_n_trab   			on (dc.c016     = moti_n_trab.C016_id)
	left join depara_respostas depara32  	on (dc.C017A    = depara32.respostas_id)
	left join f001 domicilio				on (dc.F001     = domicilio.F001_id)



select * from pnad_covid_view pcv 























