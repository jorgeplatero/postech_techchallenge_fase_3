-- CREATE TABLE `depara_resultado_covid` (
-- `id` int NOT NULL AUTO_INCREMENT,
--  `resultado_id` int DEFAULT NULL,
--  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
--  PRIMARY KEY (`id`) USING BTREE,
--  UNIQUE KEY `resultado_id_name` (`resultado_id`,`name`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- INSERT INTO `depara_resultado_covid` VALUES (1,1,'Positivo'),(2,2,'Negativo'),(3,3,'Inconclusivo'),(4,4,'Ainda não recebeu o resultado'),(5,9,'Ignorado');

select 
	cast(concat(`dc`.`Ano`,'-',`dc`.`V1013`,'-01') as date) AS `data`,
	ifnull(`uf`.`name`,'Não Identificado')  				AS `uf`,
	ifnull(`cap`.`name`,'Não Identificado')					AS `capital`,
	`situ_domi`.`name` 										AS `situacao_domicilio`,
	ifnull(`reg_metro`.`name`,'Não Aplicável') 				AS `regiao_metropolitana`,
	`tp_area`.`name` 										AS `tipo_area`,
	`cond_domi`.`name`										AS `condicao_domicilio`,
	`dc`.`A002` 											AS `idade`,
	`sexo`.`name` 											AS `sexo`,
	`raca`.`name` 											AS `cor_raca`,
	`esco`.`name` 											AS `escolaridade`,
	ifnull(`depara1`.`name`,'Não Aplicável') 				AS `sintoma_febre`,
	ifnull(`depara2`.`name`,'Não Aplicável') 				AS `sintoma_tosse`,
	ifnull(`depara3`.`name`,'Não Aplicável') 				AS `sintoma_garganta`,
	ifnull(`depara4`.`name`,'Não Aplicável') 				AS `sintoma_dif_respirar`,
	ifnull(`depara5`.`name`,'Não Aplicável') 				AS `sintoma_dor_cabeca`,
	ifnull(`depara6`.`name`,'Não Aplicável') 				AS `sintoma_dor_peito`,
	ifnull(`depara7`.`name`,'Não Aplicável') 				AS `sintoma_nausea`,
	ifnull(`depara8`.`name`,'Não Aplicável') 				AS `sintoma_coriza`,
	ifnull(`depara9`.`name`,'Não Aplicável') 				AS `sintoma_fadiga`,
	ifnull(`depara10`.`name`,'Não Aplicável') 				AS `sintoma_dor_olhos`,
	ifnull(`depara11`.`name`,'Não Aplicável') 				AS `sintoma_cheiro_sabor`,
	ifnull(`depara12`.`name`,'Não Aplicável') 				AS `sintoma_dor_muscular`,
	ifnull(`depara33`.`name`,'Não Aplicável') 				AS `sintoma_diarreia`,	
	ifnull(`depara13`.`name`,'Não Aplicável') 				AS `questao_estabelecimento_saude`,
	ifnull(`depara14`.`name`,'Não Aplicável') 				AS `questao_permaneceu_casa`,
	ifnull(`depara15`.`name`,'Não Aplicável') 				AS `questao_contato_saude`,
	ifnull(`depara16`.`name`,'Não Aplicável') 				AS `questao_remedio_conta_propria`,
	ifnull(`depara17`.`name`,'Não Aplicável') 				AS `questao_remedio_orientacao_medica`,
	ifnull(`depara18`.`name`,'Não Aplicável') 				AS `questao_visita_sus`,
	ifnull(`depara19`.`name`,'Não Aplicável') 				AS `questao_visita_participar`,
	ifnull(`depara20`.`name`,'Não Aplicável') 				AS `questao_outras_providencias`,
	ifnull(`depara21`.`name`,'Não Aplicável') 				AS `questao_buscou_atendimento`,
	ifnull(`depara22`.`name`,'Não Aplicável') 				AS `questao_buscou_PS_SUS_UPA`,
	ifnull(`depara23`.`name`,'Não Aplicável') 				AS `questao_hospital_SUS`,
	ifnull(`depara24`.`name`,'Não Aplicável') 				AS `questao_atendimento_privado`,
	ifnull(`depara25`.`name`,'Não Aplicável') 				AS `questao_ps_privado`,
	ifnull(`depara26`.`name`,'Não Aplicável') 				AS `questao_hospital_privado`,
	ifnull(`depara27`.`name`,'Não Aplicável') 				AS `questao_internacao_ajuda_respirar`,
	ifnull(`depara28`.`name`,'Não Aplicável') 				AS `questao_plano_saude`,
	ifnull(`depara29`.`name`,'Não Aplicável') 				AS `questao_trabalhou_semana_passada`,
	ifnull(`depara30`.`name`,'Não Aplicável') 				AS `questao_afastado_semana_passada`,
	ifnull(`motivo_afast`.`name`,'Não Aplicável') 			AS `questao_motivo_afastamento`,
	ifnull(`remunerado`.`name`,'Não Aplicável') 			AS `questao_trabalha_remunerado`,
	ifnull(`afastado`.`name`,'Não Aplicável') 				AS `questao_tempo_afastado_trab`,
	`dc`.`C0051`	 										AS `afastado_1mes_1ano`,
	`dc`.`C0052` 											AS `afastado_1ano_2anos`,
	`dc`.`C0053` 											AS `afastado_02anos_98anos`,
	ifnull(`depara31`.`name`,'Não Aplicável') 				AS `questao_mais_de_um_trabalho`,
	ifnull(`descr_trab`.`name`,'Não Aplicável') 			AS `questao_descricao_trabalho`,
	ifnull(`area_trab`.`name`,'Não Aplicável') 				AS `questao_area_trabalho`,
	ifnull(`tipo_trab`.`name`,'Não Aplicável') 				AS `questao_carteira_assinada_outros`,
	ifnull(`descr_tipo_trab`.`name`,'Não Aplicável') 		AS `questao_tipo_trabalho_realizado`,
	(case 
		when (`dc`.`C010` = 1) then `rendimento`.`name` 
			else 'Não aplicável' end) 						AS `faixa_rendimento`,
	(case 
		when (`dc`.`C01012` = 2) then `rendimento_prod`.`name` 
			else 'Não aplicável' end) 						AS `faixa_rendimento_retirada_produtos`,
	ifnull(`beneficio`.`name`,'Não Aplicável') AS `recebia_beneficios`,
	(case 
		when (`dc`.`C011A` = 1) then `remuneracao_trab`.`name` 
			else 'Não aplicável' end) 						AS `remuneracao_produtos_mercadoria`,
	ifnull(`moti_n_trab`.`name`,'Não Aplicável') AS `questao_moti_nao_procurar_trabalho`,
	ifnull(`depara32`.`name`,'Não Aplicável') AS `questao_gostaria_procurar_trabalho`,
	(case 
		when ((`dc`.`D0011` = 1) and (`dc`.`D0013` is not null)) then `dc`.`D0013` 
		when (`dc`.`D0011` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `rendimento_aposentadoria_pensao`,
	(case 
		when ((`dc`.`D0021` = 1) and (`dc`.`D0023` is not null)) then `dc`.`D0023` 
		when (`dc`.`D0021` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `rendimento_pensao`,
	(case 
		when ((`dc`.`D0031` = 1) and (`dc`.`D0033` is not null)) then `dc`.`D0033` 
		when (`dc`.`D0031` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `rendimento_bolsa_familia`,
	(case 
		when ((`dc`.`D0041` = 1) and (`dc`.`D0043` is not null)) then `dc`.`D0043` 
		when (`dc`.`D0041` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `rendimento_beneficios`,
	(case 
		when ((`dc`.`D0051` = 1) and (`dc`.`D0053` is not null)) then `dc`.`D0053` 
		when (`dc`.`D0051` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `auxlio_emergencia_covid`,
	(case 
		when ((`dc`.`D0061` = 1) and (`dc`.`D0063` is not null)) then `dc`.`D0063` 
		when (`dc`.`D0061` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `seguro_desemprego`,
	(case 
		when ((`dc`.`D0071` = 1) and (`dc`.`D0073` is not null)) then `dc`.`D0073` 
		when (`dc`.`D0071` = 2) then 'Não' 
			else 'Não aplicável' end) 						AS `redimentos_diversos`,
	ifnull(`domicilio`.`name`, 'Não Aplicável') 			AS `tipo_domicilio`,
	ifnull(`dc`.`F0021`,'Não Aplicável') 					AS `valor_pago_domicilio`,
	(case
		when dc.B0011  = 1 then 'Sim'
		when dc.B0012  = 1 then 'Sim'
		when dc.B0013  = 1 then 'Sim'
		when dc.B0014  = 1 then 'Sim'
		when dc.B0015  = 1 then 'Sim'
		when dc.B0016  = 1 then 'Sim'
		when dc.B0017  = 1 then 'Sim'
		when dc.B0018  = 1 then 'Sim'
		when dc.B0019  = 1 then 'Sim'
		when dc.B00110 = 1 then 'Sim'
		when dc.B00111 = 1 then 'Sim'
		when dc.B00112 = 1 then 'Sim'
		when dc.B00113 = 1 then 'Sim'
			else 'Não' end) 								AS `sintoma_covid`,
	ifnull(depara35.name,'Não Aplicável')					AS `teste_covid`, 
	(case
		when dc.B009A = 1 then 'SWAB'
		when dc.B009C = 1 then 'Sangue - Furo Dedo'
		when dc.B009E = 1 then 'Sangue - Veia do Braço'
			else 'Não Aplicável'  end) 						AS `tipo_teste`,
    (case
		when dc.B0101 = 1 then 'Sim'
		when dc.B0102 = 1 then 'Sim'
		when dc.B0103 = 1 then 'Sim'
        when dc.B0104 = 1 then 'Sim'
		when dc.B0106 = 1 then 'Sim'
		when dc.A002 >= 60 then 'Sim'
			else 'Não' end) 						AS `fator_risco_covid`,
	(case
		when dc.B005 = 1 then 'Sim'
		when dc.B005 = 3 then 'Não foi atendido'
			else 'Não'end)									AS `internado`,
	ifnull(`depara34`.`name`,'Não Aplicável')				AS `internado_ajuda_respirar`
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
	left join `depara_respostas` `depara13` on((`dc`.`B002` 	= `depara13`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara14` on((`dc`.`B0031` 	= `depara14`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara15` on((`dc`.`B0032` 	= `depara15`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara16` on((`dc`.`B0033` 	= `depara16`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara17` on((`dc`.`B0034` 	= `depara17`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara18` on((`dc`.`B0035` 	= `depara18`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara19` on((`dc`.`B0036` 	= `depara19`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara20` on((`dc`.`B0037` 	= `depara20`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara21` on((`dc`.`B0041` 	= `depara21`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara22` on((`dc`.`B0042` 	= `depara22`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara23` on((`dc`.`B0043` 	= `depara23`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara24` on((`dc`.`B0044` 	= `depara24`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara25` on((`dc`.`B0045` 	= `depara25`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara26` on((`dc`.`B0046` 	= `depara26`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara27` on((`dc`.`B006` 	= `depara27`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara28` on((`dc`.`B007`		= `depara28`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara29` on((`dc`.`C001` 	= `depara29`.`RESPOSTAS_id`))) 
	left join `depara_respostas` `depara30` on((`dc`.`C002` 	= `depara30`.`RESPOSTAS_id`))) 
	left join `c003` `motivo_afast` 		on((`dc`.`C003` 	= `motivo_afast`.`C003_id`))) 
	left join `c004` `remunerado` 			on((`dc`.`C004` 	= `remunerado`.`C004_id`))) 
	left join `c005` `afastado` 			on((`dc`.`C005` 	= `afastado`.`C005_id`))) 
	left join `depara_respostas` `depara31` on((`dc`.`C006` 	= `depara31`.`RESPOSTAS_id`))) 
	left join `c007` `descr_trab` 			on((`dc`.`C007` 	= `descr_trab`.`C007_id`))) 
	left join `c007a` `area_trab` 			on((`dc`.`C007A` 	= `area_trab`.`C007A_id`))) 
	left join `c007b` `tipo_trab` 			on((`dc`.`C007B` 	= `tipo_trab`.`C007B_id`))) 
	left join `c007c` `descr_tipo_trab` 	on((`dc`.`C007C` 	= `descr_tipo_trab`.`C007C_id`))) 
	left join `c01011` `rendimento` 		on((`dc`.`C01011`	= `rendimento`.`C01011_id`))) 
	left join `c0102` `rendimento_prod` 	on((`dc`.`C0102` 	= `rendimento_prod`.`C0102_id`))) 
	left join `c0103` `beneficio` 			on((`dc`.`C0103` 	= `beneficio`.`C0103_id`))) 
	left join `c011a11` `remuneracao_trab` 	on((`dc`.`C011A11` 	= `remuneracao_trab`.`C011A11_id`))) 
	left join `c016` `moti_n_trab` 			on((`dc`.`C016` 	= `moti_n_trab`.`C016_id`))) 
	left join `depara_respostas` `depara32` on((`dc`.`C017A` 	= `depara32`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara33` on((`dc`.`B00113` 	= `depara33`.`RESPOSTAS_id`)))
	left join `depara_respostas` `depara34` on((`dc`.`B006` 	= `depara34`.`RESPOSTAS_id`)))
	left join `f001` `domicilio` 			on((`dc`.`F001` 	= `domicilio`.`F001_id`)))
	left join `depara_respostas` `depara35`	on((`dc`.`B008` 	= `depara35`.`RESPOSTAS_id`)));