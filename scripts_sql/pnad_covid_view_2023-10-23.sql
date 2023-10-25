-- CREATE TABLE `depara_resultado_covid` (
-- `id` int NOT NULL AUTO_INCREMENT,
--  `resultado_id` int DEFAULT NULL,
--  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
--  PRIMARY KEY (`id`) USING BTREE,
--  UNIQUE KEY `resultado_id_name` (`resultado_id`,`name`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- INSERT INTO `depara_resultado_covid` VALUES (1,1,'Positivo'),(2,2,'Negativo'),(3,3,'Inconclusivo'),(4,4,'Ainda não recebeu o resultado'),(5,9,'Ignorado');

create or replace view pnad_covid_view as
select 
	cast(concat(`dc`.`Ano`,'-',`dc`.`V1013`,'-01') as date) as `data`,
	ifnull(`uf`.`name`,'Não identificado')  				as `uf`,
	`situ_domi`.`name` 										as `situacao_domicilio`,
	`dc`.`A002` 											as `idade`,
	`sexo`.`name` 											as `sexo`,
	`raca`.`name` 											as `cor_raca`,
	`esco`.`name` 											as `escolaridade`,
	ifnull(`depara1`.`name`,'Não aplicável') 				as `questao_estabelecimento_saude`,
	ifnull(`depara2`.`name`,'Não aplicável') 				as `questao_permaneceu_casa`,
	ifnull(`depara3`.`name`,'Não aplicável') 				as `questao_remedio_conta_propria`,
	ifnull(`depara4`.`name`,'Não aplicável') 				as `questao_remedio_orientacao_medica`,
	ifnull(`depara5`.`name`,'Não aplicável') 				as `questao_hospital_SUS`,
	ifnull(`depara6`.`name`,'Não aplicável') 				as `questao_hospital_privado`,
	ifnull(`depara7`.`name`, 'Não aplicável')				as `questao_internacao`,
	ifnull(`depara8`.`name`,'Não aplicável') 				as `questao_internacao_ajuda_respirar`,
	ifnull(`motivo_afast`.`name`,'Não aplicável') 			as `questao_motivo_afastamento`,
	ifnull(`afastado`.`name`,'Não aplicável') 				as `questao_tempo_afastado_trab`,
	ifnull(`descr_tipo_trab`.`name`,'Não aplicável') 		as `questao_tipo_trabalho_realizado`,
	(case 
		when (`dc`.`C010` = 1) then `rendimento`.`name` 
			else 'Não aplicável' end) 						as `faixa_rendimento`,
	(case 
		when ((`dc`.`D0011` = 1) and (`dc`.`D0013` is not null)) then `dc`.`D0013` 
		when (`dc`.`D0011` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `rendimento_aposentadoria_pensao`,
	(case 
		when ((`dc`.`D0031` = 1) and (`dc`.`D0033` is not null)) then `dc`.`D0033` 
		when (`dc`.`D0031` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `rendimento_bolsa_familia`,
	(case 
		when ((`dc`.`D0041` = 1) and (`dc`.`D0043` is not null)) then `dc`.`D0043` 
		when (`dc`.`D0041` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `rendimento_beneficios`,
	(case 
		when ((`dc`.`D0051` = 1) and (`dc`.`D0053` is not null)) then `dc`.`D0053` 
		when (`dc`.`D0051` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `auxlio_emergencia_covid`,
	(case 
		when ((`dc`.`D0061` = 1) and (`dc`.`D0063` is not null)) then `dc`.`D0063` 
		when (`dc`.`D0061` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `seguro_desemprego`,
	ifnull(`domicilio`.`name`, 'Não aplicável') 			as `tipo_domicilio`,
	ifnull(`dc`.`F0021`,'Não aplicável') 					as `valor_pago_domicilio`,
	(case
		when `dc`.`B0011`  = 1 then `depara9`.`name`
		when `dc`.`B0012`  = 1 then `depara10`.`name`
		when `dc`.`B0013`  = 1 then `depara11`.`name`
		when `dc`.`B0014`  = 1 then `depara12`.`name`
		when `dc`.`B0015`  = 1 then `depara13`.`name`
		when `dc`.`B0016`  = 1 then `depara14`.`name`
		when `dc`.`B0017`  = 1 then `depara15`.`name`
		when `dc`.`B0018`  = 1 then `depara16`.`name`
		when `dc`.`B0019`  = 1 then `depara17`.`name`
		when `dc`.`B00110` = 1 then `depara18`.`name`
		when `dc`.`B00111` = 1 then `depara19`.`name`
		when `dc`.`B00112` = 1 then `depara20`.`name`
		when `dc`.`B00113` = 1 then `depara21`.`name`
			else 'Não' end) 								as `sintoma_covid`,
	replace(
		replace(
			replace(
				concat(
				if(`dc`.`B0011` = 1, 'Febre', '-'),
				',', 
				if(`dc`.`B0012` = 1, 'Tosse', '-'),
				',', 
				if(`dc`.`B0013` = 1, 'Dor de garganta', '-'),
				',', 
				if(`dc`.`B0014` = 1, 'Dificuldade para respirar', '-'),
				',', 
				if(`dc`.`B0015` = 1, 'Dor de cabeça', '-'),
				',', 
				if(`dc`.`B0016` = 1, 'Dor no peito', '-'),
				',', 
				if(`dc`.`B0017` = 1, 'Nausea', '-'),
				',', 
				if(`dc`.`B0018` = 1, 'Coriza', '-'),
				',', 
				if(`dc`.`B0019` = 1, 'Fadiga', '-'),
				',', 
				if(`dc`.`B00110` = 1, 'Dor nos olhos', '-'),
				',', 
				if(`dc`.`B00111` = 1, 'Perda de olfato ou paladar', '-'),
				',', 
				if(`dc`.`B00112` = 1, 'Dor muscular', '-'),
				',', 
				if(`dc`.`B00113` = 1, 'Diarreia', '-')
			), ',-',''), '-,', ''), '-', '')                as 'descricao_sintoma_covid',
	ifnull(`depara22`.`name`,'Não aplicável')				as `teste_covid`, 
	replace(
		replace(
			replace(
				concat(
				if(`dc`.`B0101` = 1, 'Diabetes', '-'),
				',', 
				if(`dc`.`B0102` = 1, 'Hipertensao', '-'),
				',', 
				if(`dc`.`B0103` = 1, 'Doenca respiratoria', '-'),
				',', 
				if(`dc`.`B0104` = 1, 'Doenca cardiaca', '-'),
				',', 
				if(`dc`.`B0105` = 1, 'Depressao', '-'),
				',', 
				if(`dc`.`B0106` = 1, 'Cancer', '-'),
				',', 
				if(`dc`.`A002` >= 60, 'Idoso', '-')
				), ',-',''), '-,', ''), '-', '')            as 'descricao_fator_risco_covid',
	(case
		when `dc`.`B009A` = 1 then 'SWAB'
		when `dc`.`B009C` = 1 then 'Sangue - Furo Dedo'
		when `dc`.`B009E` = 1 then 'Sangue - Veia do Braço'
			else 'Não aplicável'  end) 						as `tipo_teste`,
    (case
		when `dc`.`B0101` = 1 then `depara23`.`name`
		when `dc`.`B0102` = 1 then `depara24`.`name`
		when `dc`.`B0103` = 1 then `depara25`.`name`
        when `dc`.`B0104` = 1 then `depara26`.`name`
		when `dc`.`B0106` = 1 then `depara27`.`name`
		when `dc`.`A002` >= 60 then 'Sim'
			else 'Não aplicável' end) 						as `fator_risco_covid`,
	(case
        when `dc`.`B009A` = 1 then `depara28`.`name`
        when `dc`.`B009C` = 1 then `depara29`.`name`
        when `dc`.`B009E` = 1 then `depara30`.`name`
            else 'Não aplicável' end)                       as `resultado_teste`
	from (((((((((((((((((((((((((((((((((((((((((((((((((((
	`dados_covid` `dc` 
	left join `uf` 							on((`dc`.`UF` 		= `uf`.`UF_id`))) 
	left join `capital` `cap` 				on((`dc`.`CAPITAL` 	= `cap`.`CAPITAL_id`))) 
	left join `v1022` `situ_domi` 			on((`dc`.`V1022` 	= `situ_domi`.`V1022_id`))) 
	left join `rm_ride` `reg_metro` 		on((`dc`.`RM_RIDE`	= `reg_metro`.`RM_RIDE_id`))) 
	left join `v1023` `tp_area` 			on((`dc`.`V1023` 	= `tp_area`.`V1023_id`))) 
	left join `a001a` `cond_domi` 			on((`dc`.`A001A` 	= `cond_domi`.`A001A_id`))) 
	left join `a003` `sexo` 				on((`dc`.`A003` 	= `sexo`.`A003_id`))) 
	left join `a004` `raca` 				on((`dc`.`A004` 	= `raca`.`A004_id`))) 
	left join `a005` `esco` 				on((`dc`.`A005` 	= `esco`.`A005_id`)))
	left join `depara_respostas` `depara1` on((`dc`.`B002` 	    = `depara1`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara2` on((`dc`.`B0031` 	= `depara2`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara3` on((`dc`.`B0033` 	= `depara3`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara4` on((`dc`.`B0034` 	= `depara4`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara5` on((`dc`.`B0043` 	= `depara5`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara6` on((`dc`.`B0046` 	= `depara6`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara7` on((`dc`.`B005` 	    = `depara7`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara8` on((`dc`.`B006` 	    = `depara8`.`RESPOSTAS_id`))) 
	left join `c003` `motivo_afast` 		on((`dc`.`C003` 	= `motivo_afast`.`C003_id`))) 
	left join `c004` `remunerado` 			on((`dc`.`C004` 	= `remunerado`.`C004_id`))) 
	left join `c005` `afastado` 			on((`dc`.`C005` 	= `afastado`.`C005_id`))) 
	left join `c007` `descr_trab` 			on((`dc`.`C007` 	= `descr_trab`.`C007_id`))) 
	left join `c007a` `area_trab` 			on((`dc`.`C007A` 	= `area_trab`.`C007A_id`))) 
	left join `c007b` `tipo_trab` 			on((`dc`.`C007B` 	= `tipo_trab`.`C007B_id`))) 
	left join `c007c` `descr_tipo_trab` 	on((`dc`.`C007C` 	= `descr_tipo_trab`.`C007C_id`))) 
	left join `c01011` `rendimento` 		on((`dc`.`C01011`	= `rendimento`.`C01011_id`))) 
	left join `c0102` `rendimento_prod` 	on((`dc`.`C0102` 	= `rendimento_prod`.`C0102_id`))) 
	left join `c0103` `beneficio` 			on((`dc`.`C0103` 	= `beneficio`.`C0103_id`))) 
	left join `c011a11` `remuneracao_trab` 	on((`dc`.`C011A11` 	= `remuneracao_trab`.`C011A11_id`))) 
	left join `c016` `moti_n_trab` 			on((`dc`.`C016` 	= `moti_n_trab`.`C016_id`)))
	left join `f001` `domicilio` 			on((`dc`.`F001` 	= `domicilio`.`F001_id`)))
    left join `depara_respostas` `depara9`	on((`dc`.`B0011` 	= `depara9`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara10`	on((`dc`.`B0012` 	= `depara10`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara11`	on((`dc`.`B0013` 	= `depara11`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara12`	on((`dc`.`B0014` 	= `depara12`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara13`	on((`dc`.`B0015` 	= `depara13`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara14`	on((`dc`.`B0016` 	= `depara14`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara15`	on((`dc`.`B0017` 	= `depara15`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara16`	on((`dc`.`B0018` 	= `depara16`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara17`	on((`dc`.`B0019` 	= `depara17`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara18`	on((`dc`.`B00110` 	= `depara18`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara19`	on((`dc`.`B00111` 	= `depara19`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara20`	on((`dc`.`B00112` 	= `depara20`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara21`	on((`dc`.`B00113` 	= `depara21`.`RESPOSTAS_id`)))
    left join `depara_respostas` `depara22`	on((`dc`.`B008` 	= `depara22`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara23`	on((`dc`.`B0101` 	= `depara23`.`RESPOSTAS_id`)))	
	left join `depara_respostas` `depara24`	on((`dc`.`B0102` 	= `depara24`.`RESPOSTAS_id`)))	
	left join `depara_respostas` `depara25`	on((`dc`.`B0103` 	= `depara25`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara26`	on((`dc`.`B0104` 	= `depara26`.`RESPOSTAS_id`)))	
	left join `depara_respostas` `depara37`	on((`dc`.`B0106` 	= `depara27`.`RESPOSTAS_id`)))
	left join `depara_resultado_covid` `depara28` on((`dc`.`B009B` = `depara28`.`RESPOSTAS_id`)))
	left join `depara_resultado_covid` `depara29` on((`dc`.`B009D` = `depara29`.`RESPOSTAS_id`)))
	left join `depara_resultado_covid` `depara30` on((`dc`.`B009F` = `depara30`.`RESPOSTAS_id`))
where 
	`dc`.`Ano` = 2020 and `dc`.`V1013` >= 09
order by 
	`dc`.`V1013`;