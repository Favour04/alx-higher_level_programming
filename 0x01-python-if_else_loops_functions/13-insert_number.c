#include <stdlib.h>
#include "lists.h"
#include <stdio.h>
/**
 * insert_node - insert node to a sorted link list
 * @head: pointer to head of list
 * @number: number to add
 * Return: new
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	current = *head;
	temp = current;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	while (current->next != NULL)
	{
		if (number < 0 ||  *head == NULL)
		{
			new->next = current;
			new->n = number;
			*head = new;
			return (new);
		}
		else if (number < current->next->n)
		{
			temp = current->next;
			new->next = temp;
			new->n = number;
			current->next = new;

			return (new);
		}
		current = current->next;
	}
	new->next = NULL;
	new->n = number;
	current->next = new;
	return (new);
}
