-- CREATE TABLE `depara_resultado_covid` (
-- `id` int NOT NULL AUTO_INCREMENT,
--  `resultado_id` int DEFAULT NULL,
--  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
--  PRIMARY KEY (`id`) USING BTREE,
--  UNIQUE KEY `resultado_id_name` (`resultado_id`,`name`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- INSERT INTO `depara_resultado_covid` VALUES (1,1,'Positivo'),(2,2,'Negativo'),(3,3,'Inconclusivo'),(4,4,'Ainda não recebeu o resultado'),(5,9,'Ignorado');

create or replace view pnad_covid_view_completa as
select 
	cast(concat(`dc`.`Ano`,'-',`dc`.`V1013`,'-01') as date) as `data`,
	ifnull(`uf`.`name`,'Não identificado')  				as `uf`,
	ifnull(`cap`.`name`,'Não identificado')					as `capital`,
	`situ_domi`.`name` 										as `situacao_domicilio`,
	ifnull(`reg_metro`.`name`,'Não aplicável') 				as `regiao_metropolitana`,
	`tp_area`.`name` 										as `tipo_area`,
	`cond_domi`.`name`										as `condicao_domicilio`,
	`dc`.`A002` 											as `idade`,
	`sexo`.`name` 											as `sexo`,
	`raca`.`name` 											as `cor_raca`,
	`esco`.`name` 											as `escolaridade`,
	ifnull(`depara1`.`name`,'Não aplicável') 				as `sintoma_febre`,
	ifnull(`depara2`.`name`,'Não aplicável') 				as `sintoma_tosse`,
	ifnull(`depara3`.`name`,'Não aplicável') 				as `sintoma_garganta`,
	ifnull(`depara4`.`name`,'Não aplicável') 				as `sintoma_dif_respirar`,
	ifnull(`depara5`.`name`,'Não aplicável') 				as `sintoma_dor_cabeca`,
	ifnull(`depara6`.`name`,'Não aplicável') 				as `sintoma_dor_peito`,
	ifnull(`depara7`.`name`,'Não aplicável') 				as `sintoma_nausea`,
	ifnull(`depara8`.`name`,'Não aplicável') 				as `sintoma_coriza`,
	ifnull(`depara9`.`name`,'Não aplicável') 				as `sintoma_fadiga`,
	ifnull(`depara10`.`name`,'Não aplicável') 				as `sintoma_dor_olhos`,
	ifnull(`depara11`.`name`,'Não aplicável') 				as `sintoma_cheiro_sabor`,
	ifnull(`depara12`.`name`,'Não aplicável') 				as `sintoma_dor_muscular`,
	ifnull(`depara13`.`name`,'Não aplicável') 				as `sintoma_diarreia`,	
	(case
		when `dc`.`B0011`  = 1 then `depara1`.`name`
		when `dc`.`B0012`  = 1 then `depara1`.`name`
		when `dc`.`B0013`  = 1 then `depara3`.`name`
		when `dc`.`B0014`  = 1 then `depara4`.`name`
		when `dc`.`B0015`  = 1 then `depara5`.`name`
		when `dc`.`B0016`  = 1 then `depara6`.`name`
		when `dc`.`B0017`  = 1 then `depara7`.`name`
		when `dc`.`B0018`  = 1 then `depara8`.`name`
		when `dc`.`B0019`  = 1 then `depara9`.`name`
		when `dc`.`B00110` = 1 then `depara10`.`name`
		when `dc`.`B00111` = 1 then `depara11`.`name`
		when `dc`.`B00112` = 1 then `depara12`.`name`
		when `dc`.`B00113` = 1 then `depara13`.`name`
			else 'Não aplicável' end) 						as `sintoma_covid`,
	ifnull(`depara14`.`name`,'Não aplicável') 				as `questao_estabelecimento_saude`,
	ifnull(`depara15`.`name`,'Não aplicável') 				as `questao_permaneceu_casa`,
	ifnull(`depara16`.`name`,'Não aplicável') 				as `questao_contato_saude`,
	ifnull(`depara17`.`name`,'Não aplicável') 				as `questao_remedio_conta_propria`,
	ifnull(`depara18`.`name`,'Não aplicável') 				as `questao_remedio_orientacao_medica`,
	ifnull(`depara19`.`name`,'Não aplicável') 				as `questao_visita_sus`,
	ifnull(`depara20`.`name`,'Não aplicável') 				as `questao_visita_participar`,
	ifnull(`depara21`.`name`,'Não aplicável') 				as `questao_outras_providencias`,
	ifnull(`depara22`.`name`,'Não aplicável') 				as `questao_buscou_atendimento`,
	ifnull(`depara23`.`name`,'Não aplicável') 				as `questao_buscou_PS_SUS_UPA`,
	ifnull(`depara24`.`name`,'Não aplicável') 				as `questao_hospital_SUS`,
	ifnull(`depara25`.`name`,'Não aplicável') 				as `questao_atendimento_privado`,
	ifnull(`depara26`.`name`,'Não aplicável') 				as `questao_ps_privado`,
	ifnull(`depara27`.`name`,'Não aplicável') 				as `questao_hospital_privado`,
	ifnull(`depara29`.`name`,'Não aplicável') 				as `questao_plano_saude`,
	ifnull(`depara30`.`name`,'Não aplicável') 				as `questao_trabalhou_semana_passada`,
	ifnull(`depara31`.`name`,'Não aplicável') 				as `questao_afastado_semana_passada`,
	ifnull(`motivo_afast`.`name`,'Não aplicável') 			as `questao_motivo_afastamento`,
	ifnull(`remunerado`.`name`,'Não aplicável') 			as `questao_trabalha_remunerado`,
	ifnull(`afastado`.`name`,'Não aplicável') 				as `questao_tempo_afastado_trab`,
	`dc`.`C0051`	 										as `afastado_1mes_1ano`,
	`dc`.`C0052` 											as `afastado_1ano_2anos`,
	`dc`.`C0053` 											as `afastado_02anos_98anos`,
	ifnull(`depara32`.`name`,'Não aplicável') 				as `questao_mais_de_um_trabalho`,
	ifnull(`descr_trab`.`name`,'Não aplicável') 			as `questao_descricao_trabalho`,
	ifnull(`area_trab`.`name`,'Não aplicável') 				as `questao_area_trabalho`,
	ifnull(`tipo_trab`.`name`,'Não aplicável') 				as `questao_carteira_assinada_outros`,
	ifnull(`descr_tipo_trab`.`name`,'Não aplicável') 		as `questao_tipo_trabalho_realizado`,
	(case 
		when (`dc`.`C010` = 1) then `rendimento`.`name` 
			else 'Não aplicável' end) 						as `faixa_rendimento`,
	(case 
		when (`dc`.`C01012` = 2) then `rendimento_prod`.`name` 
			else 'Não aplicável' end) 						as `faixa_rendimento_retirada_produtos`,
	ifnull(`beneficio`.`name`,'Não aplicável') as `recebia_beneficios`,
	(case 
		when (`dc`.`C011A` = 1) then `remuneracao_trab`.`name` 
			else 'Não aplicável' end) 						as `remuneracao_produtos_mercadoria`,
	ifnull(`moti_n_trab`.`name`,'Não aplicável') as `questao_moti_nao_procurar_trabalho`,
	ifnull(`depara33`.`name`,'Não aplicável') as `questao_gostaria_procurar_trabalho`,
	(case 
		when ((`dc`.`D0011` = 1) and (`dc`.`D0013` is not null)) then `dc`.`D0013` 
		when (`dc`.`D0011` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `rendimento_aposentadoria_pensao`,
	(case 
		when ((`dc`.`D0021` = 1) and (`dc`.`D0023` is not null)) then `dc`.`D0023` 
		when (`dc`.`D0021` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `rendimento_pensao`,
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
	(case 
		when ((`dc`.`D0071` = 1) and (`dc`.`D0073` is not null)) then `dc`.`D0073` 
		when (`dc`.`D0071` = 2) then 'Não' 
			else 'Não aplicável' end) 						as `redimentos_diversos`,
	ifnull(`domicilio`.`name`, 'Não aplicável') 			as `tipo_domicilio`,
	ifnull(`dc`.`F0021`,'Não aplicável') 					as `valor_pago_domicilio`,
    (case
		when `dc`.`B0101` = 1 then 'Sim'
		when `dc`.`B0102` = 1 then 'Sim'
		when `dc`.`B0103` = 1 then 'Sim'
        when `dc`.`B0104` = 1 then 'Sim'
		when `dc`.`B0106` = 1 then 'Sim'
		when `dc`.`A002` >= 60 then 'Sim'
			else 'Não' end) 								as `fator_risco_covid`,
	(case
		when `dc`.`B005` = 1 then 'Sim'
		when `dc`.`B005` = 2 then 'Não'
		when `dc`.`B005` = 3 then 'Não foi atendido'
		when `dc`.`B005` = 9 then 'Ignorado'
			else 'Não aplicável' end)						as `questao_internacao`,
	ifnull(`depara34`.`name`,'Não aplicável')				as `questao_internacao_ajuda_respirar`,
	ifnull(`depara35`.`name`,'Não aplicável')				as `teste_covid`, 
	(case
		when `dc`.`B009A` = 1 then 'SWAB'
		when `dc`.`B009C` = 1 then 'Sangue - Furo Dedo'
		when `dc`.`B009E` = 1 then 'Sangue - Veia do Braço'
			else 'Não aplicável'  end) 						as `tipo_teste`
from (((((((((((((((((((((((((((((((((((((((((((((((((((((((((
	`dados_covid` `dc` 
	left join `uf` 							on((`dc`.`UF` 		= `uf`.`id`))) 
	left join `capital` `cap` 				on((`dc`.`CAPITAL` 	= `cap`.`CAPITAL_id`))) 
	left join `v1022` `situ_domi` 			on((`dc`.`V1022` 	= `situ_domi`.`V1022_id`))) 
	left join `rm_ride` `reg_metro` 		on((`dc`.`RM_RIDE`	= `reg_metro`.`RM_RIDE_id`))) 
	left join `v1023` `tp_area` 			on((`dc`.`V1023` 	= `tp_area`.`V1023_id`))) 
	left join `a001a` `cond_domi` 			on((`dc`.`A001A` 	= `cond_domi`.`A001A_id`))) 
	left join `a003` `sexo` 				on((`dc`.`A003` 	= `sexo`.`A003_id`))) 
	left join `a004` `raca` 				on((`dc`.`A004` 	= `raca`.`A004_id`))) 
	left join `a005` `esco` 				on((`dc`.`A005` 	= `esco`.`A005_id`)))
	left join `depara_respostas` `depara1` 	on((`dc`.`B0011` 	= `depara1`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara2` 	on((`dc`.`B0012` 	= `depara2`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara3` 	on((`dc`.`B0013` 	= `depara3`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara4` 	on((`dc`.`B0014` 	= `depara4`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara5` 	on((`dc`.`B0015` 	= `depara5`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara6` 	on((`dc`.`B0016`	= `depara6`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara7` 	on((`dc`.`B0017` 	= `depara7`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara8` 	on((`dc`.`B0018` 	= `depara8`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara9` 	on((`dc`.`B0019` 	= `depara9`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara10`	on((`dc`.`B00110` 	= `depara10`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara11` on((`dc`.`B00111` 	= `depara11`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara12` on((`dc`.`B00112` 	= `depara12`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara13` on((`dc`.`B00113` 	= `depara13`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara14` on((`dc`.`B002` 	= `depara14`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara15` on((`dc`.`B0031` 	= `depara15`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara16` on((`dc`.`B0032` 	= `depara16`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara17` on((`dc`.`B0033` 	= `depara17`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara18` on((`dc`.`B0034` 	= `depara18`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara19` on((`dc`.`B0035` 	= `depara19`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara20` on((`dc`.`B0036` 	= `depara20`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara21` on((`dc`.`B0037` 	= `depara21`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara22` on((`dc`.`B0041` 	= `depara22`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara23` on((`dc`.`B0042` 	= `depara23`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara24` on((`dc`.`B0043` 	= `depara24`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara25` on((`dc`.`B0044` 	= `depara25`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara26` on((`dc`.`B0045` 	= `depara26`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara27` on((`dc`.`B0046` 	= `depara27`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara28` on((`dc`.`B006` 	= `depara28`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara29` on((`dc`.`B007`		= `depara29`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara30` on((`dc`.`C001` 	= `depara30`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara31` on((`dc`.`C002` 	= `depara31`.`RESPOSTAS_id`))) 
	left join `c003` `motivo_afast` 		on((`dc`.`C003` 	= `motivo_afast`.`C003_id`))) 
	left join `c004` `remunerado` 			on((`dc`.`C004` 	= `remunerado`.`C004_id`))) 
	left join `c005` `afastado` 			on((`dc`.`C005` 	= `afastado`.`C005_id`))) 
	left join `depara_respostas` `depara32` on((`dc`.`C006` 	= `depara32`.`RESPOSTAS_id`))) 
	left join `c007` `descr_trab` 			on((`dc`.`C007` 	= `descr_trab`.`C007_id`)))
	left join `c007a` `area_trab` 			on((`dc`.`C007A` 	= `area_trab`.`C007A_id`)))
	left join `c007b` `tipo_trab` 			on((`dc`.`C007B` 	= `tipo_trab`.`C007B_id`)))
	left join `c007c` `descr_tipo_trab` 	on((`dc`.`C007C` 	= `descr_tipo_trab`.`C007C_id`))) 
	left join `c01011` `rendimento` 		on((`dc`.`C01011`	= `rendimento`.`C01011_id`))) 
	left join `c0102` `rendimento_prod` 	on((`dc`.`C0102` 	= `rendimento_prod`.`C0102_id`))) 
	left join `c0103` `beneficio` 			on((`dc`.`C0103` 	= `beneficio`.`C0103_id`))) 
	left join `c011a11` `remuneracao_trab` 	on((`dc`.`C011A11` 	= `remuneracao_trab`.`C011A11_id`))) 
	left join `c016` `moti_n_trab` 			on((`dc`.`C016` 	= `moti_n_trab`.`C016_id`))) 
	left join `depara_respostas` `depara33` on((`dc`.`C017A` 	= `depara33`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara34` on((`dc`.`B006` 	= `depara34`.`RESPOSTAS_id`)))
	left join `f001` `domicilio` 			on((`dc`.`F001` 	= `domicilio`.`F001_id`)))
	left join `depara_respostas` `depara35`	on((`dc`.`B008` 	= `depara35`.`RESPOSTAS_id`)))
where 
	`dc`.`Ano` = 2020 and `dc`.`V1013` >= 09
order by 
	`dc`.`V1013`;